<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router';

const { title, rightText } = defineProps({
    title: {
        type: String,
    },
    rightText: {
        type: String,
    }
});

const router = useRouter();
const route = useRoute();

const back = () => {
    // 从修改密码界面进入编辑资料页面 回退时 退到进入修改密码之前
    if (router.options.history.state.back === '/user/password') return router.go(-2);
    router.back();
};
</script>

<template>
    <van-nav-bar
        left-arrow
        @click-left="back()"
        :right-text="rightText"
    >
        <template #title>
            <span class="title">{{ title || route.meta.title }}</span>
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
