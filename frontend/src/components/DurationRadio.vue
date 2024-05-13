<script setup lang="ts">
</script>

<template>
    <van-radio-group>
        <van-radio :name="7">近7天</van-radio>
        <van-radio :name="30">近1月</van-radio>
        <van-radio :name="90">近3月</van-radio>
        <van-radio :name="180">近6月</van-radio>
        <van-radio :name="360">近1年</van-radio>
    </van-radio-group>
</template>

<style scoped lang="less">
.van-radio-group {
    margin-bottom: 8px;
    font-size: .8rem;
}
</style>
