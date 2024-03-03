<script setup lang="ts">
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import useGlobalStore from '@/stores/global';

const globalStore = useGlobalStore();

const apps = [
    {
        icon: 'records-o',
        text: '请假',
        route: '/app/leave',
        badge: globalStore.badges.leave,
    },
    {
        icon: 'description-o',
        text: '销假',
        route: '/app/revoke',
        badge: globalStore.badges.revoke,
    },
    {
        icon: 'user-circle-o',
        text: '学生信息',
        route: '/app/student',
        badge: '',
    },
];
</script>

<template>
    <div class="client-wrapper">
        <right-slide-router-view></right-slide-router-view>
        <header class="header">
            应用
        </header>
        <van-grid square :border="false" :column-num="2" :gutter="18" icon-size="36" clickable>
            <van-grid-item v-for="app in apps" :key="app.route"
                :icon="app.icon"
                :text="app.text"
                :badge="app.badge"
                :to="app.route"
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

    .van-grid {
        --van-grid-item-content-background: #fffa;
    }
}
</style>
