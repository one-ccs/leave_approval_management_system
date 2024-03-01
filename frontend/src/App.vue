<script setup lang="ts">
import { RouterView } from 'vue-router'

</script>

<template>
    <router-view v-slot="{ Component, route }">
        <transition name="van-fade">
            <component :is="Component"></component>
        </transition>
        <bottom-menu v-if="['user', 'tools', 'contacts', 'notice'].includes(route.name as string)"></bottom-menu>
    </router-view>
</template>

<style scoped>
</style>
