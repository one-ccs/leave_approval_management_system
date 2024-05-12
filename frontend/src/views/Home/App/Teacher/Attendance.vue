<script setup lang="ts">
import BackNavBar from '@/components/BackNavBar.vue';
import Portrait from './Attendance/Portrait.vue';
import Landscape from './Attendance/Landscape.vue';

const onRightClick = () => {

};
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header" @click-right="onRightClick()">
            <template #right>
                <van-icon class-prefix="fa" name="expand" size="18"></van-icon>
                <span class="ms-2">全屏</span>
            </template>
        </back-nav-bar>
        <div class="view-container">
            <portrait />
            <landscape />
        </div>
    </div>
</template>

<style scoped lang="less">
.view {
    .view-container {
        .portrait {
            display: flex;
        }
        .landscape {
            display: none;
        }
    }
}
@media screen and (orientation: landscape) {
    .view {
        position: fixed;
        width: 100vw;

        .view-container {
            .portrait {
                display: none;
            }
            .landscape {
                display: flex;
            }
        }
    }
}
</style>
