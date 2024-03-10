<script setup lang="ts">
import { showSuccessToast } from 'vant';
import { useToggle } from '@vant/use';
import useGlobalStore from '@/stores/global';
import BackNavBar from '@/components/BackNavBar.vue';

const [choiceImagePopupShown, toggleChoiceImagePopupShown] = useToggle();

const globalStore = useGlobalStore();

const changeBackgroundImage = (index: number) => {
    globalStore.setBackgroundImageIndex(index);
    globalStore.save();
    showSuccessToast("修改成功");
};

const iconPrefix= 'fa';
const settings = [
    {
        icon: 'picture-o',
        title: '切换背景图片',
        onClick: toggleChoiceImagePopupShown,
    },
];
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <van-cell-group inset class="setting-group">
                <van-cell v-for="setting in settings" :key="setting.title"
                    size="large"
                    :icon-prefix="iconPrefix"
                    :icon="setting.icon"
                    :title="setting.title"
                    @click="setting.onClick()"
                    is-link
                ></van-cell>
            </van-cell-group>

            <van-popup v-model:show="choiceImagePopupShown"
                position="right"
                overlay-class="choice-image-popup-overlay"
                class="choice-image-popup"
            >
                <van-grid :border="false" :column-num="2" clickable>
                    <van-grid-item v-for="(imageUrl, index) in globalStore.backgroundImages">
                        <van-image class="image" :src="imageUrl" @click="changeBackgroundImage(index)"></van-image>
                    </van-grid-item>
                </van-grid>
            </van-popup>
        </div>
    </div>
</template>

<style scoped lang="less">
.view {

    .view-container {
        position: relative;
        padding: 15px 0;
        background-image: var(--bgi);
        background-size: cover;
        background-position: center top;
        background-repeat: no-repeat;

        .setting-group {
            --van-cell-group-background: #0000;
            --van-cell-background: #fffa;
        }
        .choice-image-popup-overlay {
            position: absolute;
        }
        .choice-image-popup {
            position: absolute;
            width: 75%;
            height: 100%;

            .image {
                border-radius: 8px;
                box-shadow: 1px 3px 6px 0 #333;
                overflow: hidden;
            }
        }
    }
}
</style>
