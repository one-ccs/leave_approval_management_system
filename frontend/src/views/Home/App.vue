<script setup lang="ts">
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import useGlobalStore from '@/stores/global';

const globalStore = useGlobalStore();

const apps = [
    {
        icon: 'records-o',
        text: '请假',
        route: '/app/user/leave',
        badge: globalStore.badges.leave,
        permiss: 1,
    },
    {
        icon: 'description-o',
        text: '销假',
        route: '/app/user/revoke',
        badge: globalStore.badges.revoke,
        permiss: 2,
    },
    {
        icon: 'todo-list-o',
        text: '请假历史',
        route: '/app/user/history',
        badge: '',
        permiss: 3,
    },
    {
        icon: 'user-circle-o',
        text: '学生信息',
        route: '/app/user/student',
        badge: '',
        permiss: 4,
    },
    {
        icon: 'records-o',
        text: '审批',
        route: '/app/teacher/approve',
        badge: globalStore.badges.approve,
        permiss: 5,
    },
    {
        icon: 'chart-trending-o',
        text: '考勤',
        route: '/app/teacher/attendance',
        badge: '',
        permiss: 6,
    },
    {
        icon: 'user-circle-o',
        text: '辅导员信息',
        route: '/app/teacher/teacher',
        badge: '',
        permiss: 7,
    },
    {
        icon: 'manager-o',
        text: '学生管理',
        route: '/app/admin/student',
        badge: '',
        permiss: 8,
    },
    {
        icon: 'user-o',
        text: '教师管理',
        route: '/app/admin/teacher',
        badge: '',
        permiss: 9,
    },
    {
        icon: 'cluster-o',
        text: '权限管理',
        route: '/app/admin/permission',
        badge: '',
        permiss: 10,
    },
    {
        icon: 'chat-o',
        text: '通知管理',
        route: '/app/admin/notice',
        badge: '',
        permiss: 11,
    },
    {
        icon: 'coupon-o',
        text: '失物招领管理',
        route: '/app/admin/lost',
        badge: '',
        permiss: 12,
    },
];
</script>

<template>
    <div class="client-wrapper">
        <right-slide-router-view></right-slide-router-view>
        <header class="header">
            应用
        </header>
        <van-grid class="app-grid" square :border="false" :column-num="2" :gutter="18" icon-size="3rem" clickable>
            <van-grid-item v-for="app in apps" :key="app.route"
                :icon="app.icon"
                :text="app.text"
                :badge="app.badge"
                :to="app.route"
                v-permiss="app.permiss"
            ></van-grid-item>
        </van-grid>
    </div>
</template>

<style scoped lang="less">
.client-wrapper {
    padding: 20px;
    height: 100%;
    overflow-x: hidden;
    overflow-y: auto;

    .header {
        padding: 36px 18px;
        color: #fff;
        font-size: 2.2rem;
    }
    .app-grid {
        --van-grid-item-content-background: #fffa;

        padding: 0;
        max-height: calc(100% - 117px);
        overflow-x: hidden;
        overflow-y: auto;
    }
}
</style>
