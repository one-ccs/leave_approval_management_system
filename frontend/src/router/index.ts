import { type RouteRecordRaw, createRouter, createWebHistory } from 'vue-router'
import { showToast } from 'vant';
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
                children: [
                    {
                        path: 'leave',
                        name: 'leave',
                        meta: {
                            title: '请假'
                        },
                        component: () => import('@/views/Home/App/Leave.vue'),
                    },
                    {
                        path: 'revoke',
                        name: 'revoke',
                        meta: {
                            title: '销假'
                        },
                        component: () => import('@/views/Home/App/Revoke.vue'),
                    },
                    {
                        path: 'student',
                        name: 'student',
                        meta: {
                            title: '销假'
                        },
                        component: () => import('@/views/Home/App/Student.vue'),
                    },
                ],
            },
            {
                path: '/user',
                name: 'user',
                meta: {
                    title: '用户',
                },
                component: () => import('@/views/Home/User.vue'),
                children: [
                    {
                        path: 'modify',
                        name: 'modify',
                        meta: {
                            title: '编辑资料',
                        },
                        component: () => import('@/views/Home/User/Modify.vue'),
                    },
                    {
                        path: 'password',
                        name: 'password',
                        meta: {
                            title: '修改密码',
                        },
                        component: () => import('@/views/Home/User/Password.vue'),
                    },
                    {
                        path: 'setting',
                        name: 'setting',
                        meta: {
                            title: '设置',
                        },
                        component: () => import('@/views/Home/User/Setting.vue'),
                    },
                ],
            },
        ],
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
        path: '/about',
        name: 'about',
        meta: {
            title: '关于',
        },
        component: () => import('@/views/About.vue'),
    },
    {
        path: '/:pathMatch(.*)*',
        name: '404',
        meta: {
            title: '404',
        },
        component: () => import('@/views/404.vue'),
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
        showToast("登录已过期，即将跳转登录页面...");
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
