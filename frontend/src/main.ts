import 'vant/es/toast/style';
import 'vant/es/dialog/style';
import 'vant/es/notify/style';
import 'vant/es/image-preview/style';

import 'font-awesome/css/font-awesome.min.css';

import './assets/css/main.css';

import { createApp } from 'vue';
import { Lazyload } from 'vant';

import App from './App.vue';
import pinia from './stores/pinia';
import router from './router';

import useGlobalStore from './stores/global';
import usePermissStore from './stores/permiss';
import useUserStore from './stores/user';
import useNoticeStore from './stores/notice';


// 配置 vue app
const app = createApp(App);

app.use(pinia);
app.use(router);
app.use(Lazyload);

// 异步初始化 store
setTimeout(() => {
    useNoticeStore().init();
}, 0);
// 同步初始化 store
useGlobalStore().init();
useUserStore().init();

// 自定义权限指令
const permissStore = usePermissStore();
app.directive('permiss', {
    beforeMount(el, binding) {
        if (!permissStore.hasPermiss(binding.value)) {
            el['hidden'] = true;
        }
    },
});
app.mount('#app');
