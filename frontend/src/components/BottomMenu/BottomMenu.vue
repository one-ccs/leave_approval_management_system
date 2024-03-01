<script setup lang="ts">
import { reactive } from 'vue';

const badges = reactive([
    1,2,3,4
]);
</script>

<template>
    <div class="bottom-menu">
        <div class="menu-item">
            <van-icon name="chat-o" size="24" :badge="badges[0].toString()" />
            <span class="mt-2">通知</span></div>
        <div class="menu-item">
            <van-icon name="orders-o" size="24" :badge="badges[1].toString()" />
            <span class="mt-2">通讯录</span></div>
        <div class="menu-item">
            <van-icon name="apps-o" size="24" :badge="badges[2].toString()" />
            <span class="mt-2">工作台</span>
        </div>
        <div class="menu-item">
            <van-icon name="contact-o" size="24" :badge="badges[3].toString()" />
            <span class="mt-2">我的</span>
        </div>
    </div>
</template>

<style scoped lang="less">
.bottom-menu {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-content: center;
    align-items: center;
    justify-content: space-between;

    border-top: 1px solid #3333;

    .menu-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 10px 20px;
        font-size: .72rem;
    }
}
</style>
