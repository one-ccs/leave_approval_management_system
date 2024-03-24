<script setup lang="ts">
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import BackNavBar from '@/components/BackNavBar.vue';
import NoticeCard from '@/components/NoticeCard.vue';
import { reactive } from 'vue';

const notices = reactive([
    {
        datetime: '2024-3-5 21:53:41',
        state: 0,
        title: '查寝',
        content: '那一天我二十一岁，在我一生的黄金时代。我有好多奢望。我想爱，想吃，还想在一瞬间变成天上半明半暗的云。后来我才知道，生活就是个缓慢受锤的过程，人一天天老下去，奢望也一天天消失，最后变得像挨了锤的牛一样。可是我过二十一岁生日时没有预见到这一点。我觉得自己会永远生猛下去，什么也锤不了我。',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 1,
        title: '查寝',
        content: '',
    },
]);
</script>

<template>
    <div class="view">
        <right-slide-router-view />
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <div v-if="notices.length" class="notice-list">
                <notice-card v-for="notice in notices"
                    :datetime="notice.datetime"
                    :state="notice.state"
                    :title="notice.title"
                    :content="notice.content"
                />
                <van-back-top />
            </div>
            <van-empty v-else image="search" description="暂无数据" />
        </div>
    </div>
</template>

<style scoped lang="less">
.view-container {
    padding: 15px;
}
</style>
