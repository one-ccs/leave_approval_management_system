import 'vant/es/toast/style';
import 'vant/es/dialog/style';
import 'vant/es/notify/style';
import 'vant/es/image-preview/style';

import 'font-awesome/css/font-awesome.min.css';

import './assets/main.css';

import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';

import usePermissStore from './stores/permiss';

const app = createApp(App);

app.use(createPinia());
app.use(router);

// 自定义权限指令
const permissStore = usePermissStore();
app.directive('permiss', {
    beforeMount(el, binding) {
        if (!permissStore.permiss.includes(binding.value)) {
            el.hidden = true;
        }
    },
});
app.mount('#app');
