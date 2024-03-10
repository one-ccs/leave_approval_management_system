import 'vant/es/toast/style';
import 'vant/es/dialog/style';
import 'vant/es/notify/style';
import 'vant/es/image-preview/style';

import 'font-awesome/css/font-awesome.min.css';

import './assets/main.css';

import { createApp } from 'vue';

import App from './App.vue';
import router from './router';
import pinia from './stores/pinia';

import useGlobalStore from './stores/global';
import usePermissStore from './stores/permiss';
import useUserStore from './stores/user';


// 初始化 store
useGlobalStore().init();
useUserStore().init();

// 配置 vue app
const app = createApp(App);

app.use(pinia);
app.use(router);

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
