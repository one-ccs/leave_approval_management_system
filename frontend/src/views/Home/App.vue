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
        route: '/app/assistant/approve',
        badge: badgeStore.approve,
        permiss: 5,
    },
    {
        icon: 'chart-trending-o',
        text: '查看考勤',
        route: '/app/assistant/attendance',
        badge: '',
        permiss: 6,
    },
    {
        icon: 'chat-o',
        text: '通知管理',
        route: '/app/assistant/notice',
        badge: '',
        permiss: 7,
    },
    {
        icon: 'user-circle-o',
        text: '辅导员信息',
        route: '/app/assistant/assistant',
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
        text: '辅导员管理',
        route: '/app/admin/assistant',
        badge: '',
        permiss: 10,
    },
    {
        icon: 'user-o',
        text: '管理员管理',
        route: '/app/admin/adminManager',
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
        icon: 'user-circle-o',
        text: '管理员信息',
        route: '/app/admin/admin',
        badge: '',
        permiss: 13,
    },
];
</script>

<template>
    <div class="client-wrapper">
        <right-slide-router-view />
        <header class="header">应用</header>
        <van-grid
            class="app-grids translucent-half"
            square
            :border="false"
            :column-num="2"
            icon-size="3rem"
        >
            <van-grid-item v-for="app in apps"
                class="app-box van-haptics-feedback"
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

        .app-box {
            flex-basis: calc(50% - 5px) !important;
            border-radius: var(--border-radius);
            overflow: hidden;
        }
        .app-box:nth-child(2n) {
            margin-left: auto;
        }
        .app-box {
            margin-top: 10px;
        }
    }
}
</style>
