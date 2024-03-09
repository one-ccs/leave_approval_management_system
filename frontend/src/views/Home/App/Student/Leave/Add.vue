<script setup lang="ts">
import BackNavBar from '@/components/BackNavBar.vue';

const formRules = {
    username: [
        { required: true, message: '请填写用户名' },
    ],
    password: [
        { required: true, message: '请填写密码' },
    ],
};
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header"></back-nav-bar>
        <div class="view-container">
            <van-form>

            </van-form>
        </div>
    </div>
</template>

<style scoped lang="less">
</style>
