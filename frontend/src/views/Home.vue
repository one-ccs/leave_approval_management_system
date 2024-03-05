<script setup lang="ts">
import { computed } from 'vue';
import useGlobalStore from '@/stores/global';
import Tabbar from '@/components/Tabbar.vue';

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
        <tabbar></tabbar>
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
}
</style>
