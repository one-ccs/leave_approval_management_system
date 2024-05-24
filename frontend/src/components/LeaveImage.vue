<script setup lang="ts">
import useGlobalStore from '@/stores/global';

interface Props {
    src: string | null,
    width?: string | number,
    height?: string | number,
    loadingIcon?: string,
    iconSize?: string | number,
    iconPrefix?: string,
    round?: boolean,
    lazyLoad?: boolean,
    alt?: string,
};

const props = withDefaults(defineProps<Props>(), {
    src: null,
    width: 256,
    height: 128,
    loadingIcon: 'star-o',
    iconSize: 38,
    round: false,
    lazyLoad: true,
    alt: '请假条图片',
});

const globalStore = useGlobalStore();
</script>

<template>
    <van-image
        class="leave"
        :src="props.src ? `${globalStore.apiHost}/file${props.src}` : globalStore.logoPngUrl"
        :width="props.width"
        :height="props.height"
        :error-icon="globalStore.logoPngUrl"
        :alt="props.alt"
        :round="props.round"
        :lazy-load="props.lazyLoad"
    >
        <template #loading>
            <van-loading vertical>
                <template #icon>
                    <van-icon :name="props.loadingIcon" :size="props.iconSize"></van-icon>
                </template>
            </van-loading>
        </template>
    </van-image>
</template>

<style scoped lang="less">
.avatar {
    flex: 0 0 auto;
}
</style>
