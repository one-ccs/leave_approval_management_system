<script setup lang="ts">
import Tabbar from '@/components/Tabbar.vue';
import useGlobalStore from '@/stores/global';

const globalStore = useGlobalStore();

console.log(globalStore.backgroundImage);
</script>

<template>
    <div class="view">
        <div class="client-view">
            <img :src="globalStore.backgroundImage.href" alt="背景图片" class="bgi">
            <router-view v-slot="{ Component, route }">
                <transition name="van-fade" mode="out-in">
                    <component :is="Component"></component>
                </transition>
            </router-view>
        </div>
        <tabbar></tabbar>
    </div>
</template>

<style scoped lang="less">
.view {
    .client-view {
        position: relative;
        width: 100%;
        height: calc(100% - var(--van-tabbar-height));

        .bgi {
            z-index: -1;
            position: absolute;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    }
}
</style>
