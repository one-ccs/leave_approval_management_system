<script setup lang="ts">
import useBadgeStore from '@/stores/badge';
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';

const badgeStore = useBadgeStore();

const apps = [
    {
        icon: 'records-o',
        text: '请假',
        route: '/app/student/leave',
        badge: badgeStore.leave,
        permiss: 1,
    },
    {
        icon: 'description-o',
        text: '销假',
        route: '/app/student/revoke',
        badge: badgeStore.revoke,
        permiss: 2,
    },
    {
        icon: 'todo-list-o',
        text: '请假历史',
        route: '/app/student/history',
        badge: '',
        permiss: 3,
    },
    {
        icon: 'user-circle-o',
        text: '学生信息',
        route: '/app/student/student',
        badge: '',
        permiss: 4,
    },
    {
        icon: 'records-o',
        text: '请假审批',
        route: '/app/teacher/approve',
        badge: badgeStore.approve,
        permiss: 5,
    },
    {
        icon: 'chart-trending-o',
        text: '查看考勤',
        route: '/app/teacher/attendance',
        badge: '',
        permiss: 6,
    },
    {
        icon: 'chat-o',
        text: '发布通知',
        route: '/app/teacher/notice',
        badge: '',
        permiss: 7,
    },
    {
        icon: 'user-circle-o',
        text: '辅导员信息',
        route: '/app/teacher/teacher',
        badge: '',
        permiss: 8,
    },
    {
        icon: 'manager-o',
        text: '学生管理',
        route: '/app/admin/student',
        badge: '',
        permiss: 9,
    },
    {
        icon: 'user-o',
        text: '教师管理',
        route: '/app/admin/teacher',
        badge: '',
        permiss: 10,
    },
    {
        icon: 'cluster-o',
        text: '权限管理',
        route: '/app/admin/permission',
        badge: '',
        permiss: 11,
    },
    {
        icon: 'chat-o',
        text: '通知管理',
        route: '/app/admin/notice',
        badge: '',
        permiss: 12,
    },
    {
        icon: 'coupon-o',
        text: '失物招领管理',
        route: '/app/admin/lost',
        badge: '',
        permiss: 13,
    },
];
</script>

<template>
    <div class="client-wrapper">
        <right-slide-router-view></right-slide-router-view>
        <header class="header">应用</header>
        <van-grid class="app-grids translucent-half" square :border="false" :column-num="2" :gutter="18" icon-size="3rem" clickable>
            <van-grid-item v-for="app in apps"
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
    .app-grids {
        max-height: calc(100% - 117px);
        overflow-x: hidden;
        overflow-y: auto;

        :deep(.van-grid-item__text) {
            font-size: 1rem;
        }
    }
}
</style>
