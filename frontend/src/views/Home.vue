<script setup lang="ts">
import useGlobalStore from '@/stores/global';
import { computed } from 'vue';

const globalStore = useGlobalStore();
const backgroundImage = computed(() => {
    return `url(${globalStore.backgroundImage})`;
});
</script>

<template>
    <div class="view">
        <div class="client-view">
            <router-view v-slot="{ Component, route }">
                <component :is="Component"></component>
            </router-view>
        </div>
        <van-tabbar route class="tabbar" :fixed="false" safe-area-inset-bottom>
            <van-tabbar-item
                replace
                to="/notice"
                icon="chat-o"
                :badge="globalStore.badges.notice"
            >通知</van-tabbar-item>
            <van-tabbar-item
                replace
                to="/app"
                icon="apps-o"
                :badge="globalStore.badges.app"
            >应用</van-tabbar-item>
            <van-tabbar-item
                replace
                to="/user"
                icon="contact-o"
                :badge="globalStore.badges.user"
            >我的</van-tabbar-item>
        </van-tabbar>
    </div>
</template>

<style scoped lang="less">
.view {
    .client-view {
        --bgi: v-bind(backgroundImage);

        width: 100%;
        height: calc(100% - var(--van-tabbar-height));
        background-image: var(--bgi);
        background-size: cover;
        background-position: center top;
        background-repeat: no-repeat;
    }
    .tabbar {
        --van-tabbar-background: #fff;
    }
}
</style>
