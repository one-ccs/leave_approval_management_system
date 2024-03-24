import { type RouteRecordRaw, createRouter, createWebHistory } from 'vue-router'
import { showFailToast } from 'vant';
import HomeView from '@/views/Home.vue';
import usePermissStore from '@/stores/permiss';
import useUserStore from '@/stores/user';


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
                path: 'notice',
                name: 'notice',
                meta: {
                    title: '通知',
                },
                component: () => import('@/views/Home/Notice.vue'),
                children: [
                    {
                        path: 'system',
                        name: 'noticeSystem',
                        meta: {
                            title: '系统通知',
                        },
                        component: () => import('@/views/Home/Notice/NoticeList.vue'),
                    },
                    {
                        path: 'school',
                        name: 'noticeSchool',
                        meta: {
                            title: '学校通知',
                        },
                        component: () => import('@/views/Home/Notice/NoticeList.vue'),
                    },
                    {
                        path: 'college',
                        name: 'noticeCollege',
                        meta: {
                            title: '学院通知',
                        },
                        component: () => import('@/views/Home/Notice/NoticeList.vue'),
                    },
                    {
                        path: 'teacher',
                        name: 'noticeTeacher',
                        meta: {
                            title: '辅导员通知',
                        },
                        component: () => import('@/views/Home/Notice/NoticeList.vue'),
                    },
                ],
            },
            {
                path: 'app',
                name: 'app',
                meta: {
                    title: '应用',
                },
                component: () => import('@/views/Home/App.vue'),
                children: [
                    {
                        path: 'student',
                        name: '',
                        children: [
                            {
                                path: 'leave',
                                name: 'studentLeave',
                                meta: {
                                    title: '请假',
                                    permiss: 1,
                                },
                                component: () => import('@/views/Home/App/LeaveRevokeHistoryApprove.vue'),
                                children: [
                                    {
                                        path: 'add',
                                        name: 'studentLeaveAdd',
                                        meta: {
                                            title: '请假申请',
                                        },
                                        component: () => import('@/views/Home/App/Student/Leave/Add.vue')
                                    },
                                    {
                                        path: 'detail',
                                        name: 'studentLeaveDetail',
                                        meta: {
                                            title: '请假详情',
                                        },
                                        component: () => import('@/views/Home/App/LeaveDetail.vue')
                                    },
                                ],
                            },{
                                path: 'revoke',
                                name: 'studentRevoke',
                                meta: {
                                    title: '销假',
                                    permiss: 2,
                                },
                                component: () => import('@/views/Home/App/LeaveRevokeHistoryApprove.vue'),
                                children: [
                                    {
                                        path: 'detail',
                                        name: 'studentRevokeDetail',
                                        meta: {
                                            title: '请假详情',
                                        },
                                        component: () => import('@/views/Home/App/LeaveDetail.vue')
                                    },
                                ],
                            },
                            {
                                path: 'history',
                                name: 'studentHistory',
                                meta: {
                                    title: '请假历史',
                                    permiss: 3,
                                },
                                component: () => import('@/views/Home/App/LeaveRevokeHistoryApprove.vue'),
                                children: [
                                    {
                                        path: 'detail',
                                        name: 'studentHistoryDetail',
                                        meta: {
                                            title: '请假详情',
                                        },
                                        component: () => import('@/views/Home/App/LeaveDetail.vue')
                                    },
                                ],
                            },
                            {
                                path: 'signIn',
                                name: 'studentSignIn',
                                meta: {
                                    title: '签到',
                                    permiss: 3,
                                },
                                component: () => import('@/views/Home/App/Student/SignIn.vue'),
                            },
                            {
                                path: 'student',
                                name: 'studentStudent',
                                meta: {
                                    title: '学生信息',
                                    permiss: 4,
                                },
                                component: () => import('@/views/Home/App/UserInfo.vue'),
                                children: [
                                    {
                                        path: 'record',
                                        name: 'studentStudentRecord',
                                        meta: {
                                            title: '学籍档案',
                                        },
                                        component: () => import('@/views/Home/App/Student/Record.vue'),
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        path: 'teacher',
                        name: '',
                        children: [
                            {
                                path: 'approve',
                                name: 'teacherApprove',
                                meta: {
                                    title: '请假审批',
                                    permiss: 5,
                                },
                                component: () => import('@/views/Home/App/LeaveRevokeHistoryApprove.vue'),
                                children: [
                                    {
                                        path: 'detail',
                                        name: 'teacherApproveDetail',
                                        meta: {
                                            title: '请假详情',
                                        },
                                        component: () => import('@/views/Home/App/LeaveDetail.vue')
                                    },
                                ],
                            },
                            {
                                path: 'attendance',
                                name: 'teacherAttendance',
                                meta: {
                                    title: '查看考勤',
                                    permiss: 6,
                                },
                                component: () => import('@/views/Home/App/Teacher/Attendance.vue'),
                            },
                            {
                                path: 'notice',
                                name: 'teacherNotice',
                                meta: {
                                    title: '发布通知',
                                    permiss: 7,
                                },
                                component: () => import('@/views/Home/App/Teacher/Notice.vue'),
                            },
                            {
                                path: 'teacher',
                                name: 'teacherTeacher',
                                meta: {
                                    title: '教师信息',
                                    permiss: 8,
                                },
                                component: () => import('@/views/Home/App/UserInfo.vue'),
                            },
                        ],
                    },
                    {
                        path: 'admin',
                        name: '',
                        children: [
                            {
                                path: 'student',
                                name: 'adminStudent',
                                meta: {
                                    title: '学生管理',
                                    permiss: 9,
                                },
                                component: () => import('@/views/Home/App/Admin/Student.vue'),
                                children: [
                                    {
                                        path: 'detail',
                                        name: 'adminStudentDetail',
                                        meta: {
                                            title: '学生详情',
                                        },
                                        component: () => import('@/views/Home/App/Admin/UserDetail.vue'),
                                    },
                                ],
                            },
                            {
                                path: 'teacher',
                                name: 'adminTeacher',
                                meta: {
                                    title: '教师管理',
                                    permiss: 10,
                                },
                                component: () => import('@/views/Home/App/Admin/Teacher.vue'),
                                children: [
                                    {
                                        path: 'detail',
                                        name: 'adminTeacherDetail',
                                        meta: {
                                            title: '教师详情',
                                        },
                                        component: () => import('@/views/Home/App/Admin/UserDetail.vue'),
                                    },
                                ],
                            },
                            {
                                path: 'adminManager',
                                name: 'adminAdminManager',
                                meta: {
                                    title: '管理员管理',
                                    permiss: 11,
                                },
                                component: () => import('@/views/Home/App/Admin/Admin.vue'),
                                children: [
                                    {
                                        path: 'detail',
                                        name: 'adminAdminManagerDetail',
                                        meta: {
                                            title: '管理员详情',
                                        },
                                        component: () => import('@/views/Home/App/Admin/UserDetail.vue'),
                                    },
                                ],
                            },
                            {
                                path: 'permission',
                                name: 'adminPermission',
                                meta: {
                                    title: '权限管理',
                                    permiss: 12,
                                },
                                component: () => import('@/views/Home/App/Admin/Permission.vue'),
                            },
                            {
                                path: 'notice',
                                name: 'adminNotice',
                                meta: {
                                    title: '通知管理',
                                    permiss: 13,
                                },
                                component: () => import('@/views/Home/App/Admin/Notice.vue'),
                            },
                            {
                                path: 'lost',
                                name: 'adminLost',
                                meta: {
                                    title: '失物招领管理',
                                    permiss: 14,
                                },
                                component: () => import('@/views/Home/App/Admin/Lost.vue'),
                            },
                            {
                                path: 'admin',
                                name: 'adminAdmin',
                                meta: {
                                    title: '管理员信息',
                                    permiss: 15,
                                },
                                component: () => import('@/views/Home/App/UserInfo.vue'),
                            },
                        ],
                    },
                ],
            },
            {
                path: 'user',
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
                        children: [
                            {
                                path: 'avatar',
                                name: 'modifyAvatar',
                                meta: {
                                    title: '修改头像',
                                },
                                component: () => import('@/views/Home/User/Modify/Avatar.vue'),
                            },
                            {
                                path: 'telephone',
                                name: 'modifyTelephone',
                                meta: {
                                    title: '手机号操作',
                                },
                                component: () => import('@/views/Home/User/Modify/Telephone.vue'),
                            },
                        ],
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
    const permissStore = usePermissStore();
    const userStore = useUserStore();

    if (!userStore.isLogin && !['login', 'forgot'].includes(to.name as string)) {
        // 未登录返回登录页
        next('/login');
    } else if (userStore.isLogin && userStore.isExpired()) {
        // 登录已过期
        userStore.clear();
        showFailToast("登录已过期\n请重新登录");
        next('/login');
    } else if (userStore.isLogin && to.name === 'login') {
        // 已登录禁止进入登录页
        next(from);
    } else if (to.meta.permiss && !permissStore.hasPermiss(to.meta.permiss as number)) {
        // 如果没有权限，则进入403
        next('/403');
    } else {
        // 正常跳转
        next();
    }
});


export default router;
