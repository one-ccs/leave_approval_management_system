<script setup lang="ts">
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import BackNavBar from '@/components/BackNavBar.vue';
</script>

<template>
    <div class="view">
        <right-slide-router-view></right-slide-router-view>
        <back-nav-bar class="view-header"></back-nav-bar>
        <div class="view-container">

        </div>
    </div>
</template>

<style scoped lang="less">
</style>
