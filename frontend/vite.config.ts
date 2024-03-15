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
        sourcemap: false, // 取消生成 sourcemap 可以防止在浏览器“源代码”目录树中暴露项目结构
        outDir: 'dist',
        assetsDir: 'static',
        chunkSizeWarningLimit: 800,
        reportCompressedSize: false, // 禁用 gzip 压缩大小报告
        minify: 'esbuild', // 指定混淆器
        rollupOptions: {
            output: {
                // 打包规则
                manualChunks(id) {
                    // node_modules 目录打包规则
                    if (id.includes('node_modules')) {
                        const arr = id.toString().split('node_modules/')[1].split('/')

                        switch (arr[0]) {
                            // 中文件 打包到为 static 中
                            case '@vant':
                            case 'vant':
                            case 'font-awesome':
                                return 'static';
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
                        // src 目录中的 css 和 js 全部打包为 static.css/static.js 中
                        return 'static';
                    }
                },
                // 存放路径及命名规则
                chunkFileNames: (chunkInfo) => {
                    return 'static/js/[name]-[hash].js';
                },
                entryFileNames: (chunkInfo) => {
                    return 'static/js/[name]-[hash].js';
                },
                assetFileNames: (chunkInfo) => {
                    // 修改 font-awesome 字体资源文件路径
                    if (chunkInfo.name?.includes('fontawesome-webfont')) {
                        return 'static/fonts/[ext]/[name]-[hash].[ext]';
                    }
                    return 'static/[ext]/[name]-[hash].[ext]';
                },
            },
        },
    },
});
