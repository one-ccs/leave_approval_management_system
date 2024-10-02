import { fileURLToPath, URL } from 'node:url';

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import Components from 'unplugin-vue-components/vite';
import { VantResolver } from '@vant/auto-import-resolver';
import mockDevServerPlugin from 'vite-plugin-mock-dev-server';

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        Components({
            resolvers: [
                VantResolver(),
            ],
        }),
        mockDevServerPlugin(),
    ],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url)),
        }
    },
    server: {
        host: '0.0.0.0',
        port: 5177,
        proxy: {
            "^/api": {
                target: "/",
            },
        },
    },
    build: {
        // 文件改变时自动打包
        watch: {
            include: ['src/**'],
        },
        sourcemap: false, // 取消生成 sourcemap 可以防止在浏览器“源代码”目录树中暴露项目结构
        outDir: 'dist',
        chunkSizeWarningLimit: 800,
        reportCompressedSize: false, // 禁用 gzip 压缩大小报告
        minify: 'esbuild', // 指定混淆器
        assetsInlineLimit: 4096, // 内联小于 4kb 的资源
        rollupOptions: {
            output: {
                // 打包规则
                manualChunks(id) {
                    // node_modules 目录打包规则
                    if (id.includes('node_modules')) {
                        const arr = id.toString().split('node_modules/')[1].split('/')

                        switch (arr[0]) {
                            // 中文件 打包到 main 中
                            case '@vant':
                            case 'vant':
                            case 'font-awesome':
                                return 'main';
                            // 大文件 单独打包
                            // case '':
                            //     return arr[0];
                            // 其他文件 打包到 vendor 中
                            default:
                                return 'vendor';
                        }
                    }
                    // 项目资源打包规则
                    if (id.includes('src')) {
                        // src 目录中的 css 和 js 全部打包为 main.css/main.js 中
                        return 'main';
                    }
                },
                // 存放路径及命名规则
                chunkFileNames: (chunkInfo) => {
                    return 'assets/js/[name]-[hash].js';
                },
                entryFileNames: (chunkInfo) => {
                    return 'assets/js/[name]-[hash].js';
                },
                // 修改资源文件路径
                assetFileNames: (assetInfo) => {
                    const fontExtnameList = ['.eot', '.woff', '.woff2', '.ttf'];
                    const imageExtnameList = ['.jpg', '.jpeg', '.png', '.gif', '.ico', '.svg'];

                    if (fontExtnameList.some((extname) => assetInfo.name?.endsWith(extname))) {
                        return 'assets/fonts/[name]-[hash].[ext]';
                    }
                    if (imageExtnameList.some((extname) => assetInfo.name?.endsWith(extname))) {
                        return 'assets/images/[name]-[hash].[ext]';
                    }
                    return 'assets/[ext]/[name]-[hash].[ext]';
                },
            },
        },
    },
});
