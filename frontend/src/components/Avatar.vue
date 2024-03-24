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

const {
    src, size, loadingIcon, iconSize, round, lazyLoad, alt,
} = withDefaults(defineProps<Props>(), {
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
        :src="src ? `${globalStore.apiHost}/file${src}` : globalStore.defaultAvatarUrl"
        :width="size"
        :height="size"
        :error-icon="globalStore.defaultAvatarUrl"
        :alt="alt"
        :round="round"
        :lazy-load="lazyLoad"
    >
        <template #loading>
            <van-loading vertical>
                <template #icon>
                    <van-icon :name="loadingIcon" :size="iconSize"></van-icon>
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
