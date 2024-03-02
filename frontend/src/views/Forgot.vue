<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();
</script>

<template>
    <div class="view">
        <van-nav-bar
            left-arrow
            @click-left="router.back()"
        >
            <template #title>
                <span>找回密码</span>
            </template>
        </van-nav-bar>
    </div>
</template>

<style scoped lang="less">
</style>
