import { type RouteRecordRaw, createRouter, createWebHistory } from 'vue-router'


const routes: Array<RouteRecordRaw> = [
    {
        path: '/',
        alias: ['/home', '/index', '/login'],
        name: 'login',
        component: () => import('@/views/LoginView.vue'),
    },
    {
        path: '/forgot',
        name: 'forgot',
        component: () => import('@/views/ForgotView.vue'),
    },
    {
        path: '/user',
        name: 'user',
        component: () => import('@/views/UserView.vue'),
    }
];


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});


export default router;
