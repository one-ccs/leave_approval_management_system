<script setup lang="ts">
import useGlobalStore from '@/stores/global';

const globalStore = useGlobalStore();

const items = [
    {
        icon: 'chat-o',
        text: '通知',
        link: '/notice',
        permiss: 0x1,
    },
    {
        icon: '',
        text: '',
        link: '',
        permiss: 0x4,
    },
    {
        icon: '',
        text: '',
        link: '',
        permiss: 0x8,
    },
];
</script>

<template>
    <div class="bottom-menu">
        <router-link to="notice" class="menu-item">
            <van-icon name="chat-o" size="24" :badge="globalStore.badges.notice" />
            <span class="mt-2">通知</span>
        </router-link>
        <div class="menu-item">
            <van-icon name="apps-o" size="24" :badge="globalStore.badges.app" />
            <span class="mt-2">应用</span>
        </div>
        <div class="menu-item">
            <van-icon name="contact-o" size="24" :badge="globalStore.badges.user" />
            <span class="mt-2">我的</span>
        </div>
    </div>
</template>

<style scoped lang="less">
.bottom-menu {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-content: center;
    align-items: center;
    justify-content: space-between;

    border-top: 1px solid #3333;

    .menu-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 10px 20px;
        font-size: .72rem;
    }
}
</style>
