import { type RouteRecordRaw, createRouter, createWebHistory } from 'vue-router'
import { localLoad, localRemove, sessionLoad, sessionRemove } from '@/utils/storage';
import HomeView from '@/views/Home.vue';


const routes: RouteRecordRaw[] = [
    {
        path: '/',
        redirect: '/user'
    },
    {
        path: '/',
        name: 'home',
        component: HomeView,
        children: [
            {
                path: '/notice',
                name: 'notice',
                meta: {
                    title: '通知',
                },
                component: () => import('@/views/Home/Notice.vue'),
            },
            {
                path: '/app',
                name: 'app',
                meta: {
                    title: '应用',
                },
                component: () => import('@/views/Home/App.vue'),
            },
            {
                path: '/user',
                name: 'user',
                meta: {
                    title: '用户',
                },
                component: () => import('@/views/Home/User.vue'),
            },
            {
                path: '/about',
                name: 'about',
                meta: {
                    title: '关于',
                },
                component: () => import('@/views/Home/About.vue'),
            },
        ]
    },
    {
        path: '/login',
        name: 'login',
        meta: {
            title: '登录',
        },
        component: () => import('@/views/Login.vue'),
    },
    {
        path: '/forgot',
        name: 'forgot',
        meta: {
            title: '找回密码',
        },
        component: () => import('@/views/Forgot.vue'),
    },
    {
        path: '/:pathMatch(.*)*',
        name: '404',
        component: () => import('@/views/404.vue'),
        meta: {
            title: '404',
        },
    },
];


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | 请假视频管理系统`;
    const user = localLoad('user') || sessionLoad('user');

    if (!user && !['login', 'forgot'].includes(to.name as string)) {
        // 未登录返回登录页
        next('/login');
    } else if (user && user.expires <= new Date().getTime()) {
        // 登录已过期
        localRemove('user');
        sessionRemove('user');
        next('/login');
    } else if (user && to.name === 'login') {
        // 已登录禁止进入登录页
        next(from);
    } else {
        // 正常跳转
        next();
    }
});


export default router;
