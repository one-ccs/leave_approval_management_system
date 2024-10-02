<script setup lang="ts">
import useGlobalStore from '@/stores/global';

interface Props {
    src: string | null,
    size?: string | number,
    loadingIcon?: string,
    iconSize?: string | number,
    iconPrefix?: string,
    round?: boolean,
    lazyLoad?: boolean,
    alt?: string,
};

const props = withDefaults(defineProps<Props>(), {
    src: null,
    size: 64,
    loadingIcon: 'star-o',
    iconSize: 38,
    round: true,
    lazyLoad: true,
    alt: '头像图片',
});

const globalStore = useGlobalStore();
</script>

<template>
    <van-image
        class="avatar"
        :src="props.src ? `${globalStore.apiHost}/file${props.src}` : globalStore.defaultAvatarUrl.href"
        :width="props.size"
        :height="props.size"
        :error-icon="globalStore.defaultAvatarUrl.href"
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
