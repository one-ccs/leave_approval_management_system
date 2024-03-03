<script setup lang="ts">
</script>

<template>
    <router-view v-slot="{ Component }">
        <transition name="van-slide-right">
            <component :is="Component" />
        </transition>
    </router-view>
</template>

<style scoped lang="less">
</style>
