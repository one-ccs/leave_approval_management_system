<script setup lang="ts">
import useBadgeStore from '@/stores/badge';

const badgeStore = useBadgeStore();
</script>

<template>
    <van-tabbar route class="tabbar" :fixed="false" safe-area-inset-bottom>
        <van-tabbar-item
            replace
            to="/notice"
            icon="chat-o"
            :badge="badgeStore.notice"
        >通知</van-tabbar-item>
        <van-tabbar-item
            replace
            to="/app"
            icon="apps-o"
            :badge="badgeStore.app"
        >应用</van-tabbar-item>
        <van-tabbar-item
            replace
            to="/user"
            icon="contact-o"
            :badge="badgeStore.user"
        >我的</van-tabbar-item>
    </van-tabbar>
</template>

<style scoped lang="less">
.tabbar {
    --van-tabbar-background: #fff;
}
</style>
