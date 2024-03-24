<script setup lang="ts">
import { reactive } from 'vue';
import useUserStore from '@/stores/user';
import BackNavBar from '@/components/BackNavBar.vue';
import SignInCard from '@/components/SignInCard.vue';

const userStore = useUserStore();
const notices = reactive([
    {
        datetime: '2024-3-5 21:53:41',
        state: 0,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 1,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 0,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 0,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 1,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 1,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 0,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 1,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 1,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 1,
        title: '查寝',
    },
]);
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <div  v-if="notices.length"class="notice-list">
                <sign-in-card v-for="notice in notices"
                    :datetime="notice.datetime"
                    :state="notice.state"
                    :title="notice.title"
                    :describe="userStore.userInfo._class"
                />
                <van-back-top />
            </div>
            <van-empty v-else image="search" description="暂无数据" />
        </div>
    </div>
</template>

<style scoped lang="less">
.view {
    .view-container {
        padding: 15px;
    }
}
</style>
