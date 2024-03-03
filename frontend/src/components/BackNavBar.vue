<script setup lang="ts">
import { useRouter } from 'vue-router';

const { title, rightText } = defineProps({
    title: {
        type: String,
        required: true,
    },
    rightText: {
        type: String,
    }
});

const router = useRouter();
</script>

<template>
    <van-nav-bar
        left-arrow
        @click-left="router.back()"
        :right-text="rightText"
    >
        <template #title>
            <span class="title">{{ title }}</span>
        </template>
        <template v-if="!rightText" #right>
            <slot name="right"></slot>
        </template>
    </van-nav-bar>
</template>

<style scoped lang="less">
.title {
    font-size: 1rem ;
}
</style>
