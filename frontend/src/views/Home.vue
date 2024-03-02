<script setup lang="ts">
</script>

<template>
    <router-view v-slot="{ Component, route }">
        <transition name="van-fade">
            <component :is="Component"></component>
        </transition>
    </router-view>
    <bottom-menu />
</template>

<style scoped lang="less">
</style>
