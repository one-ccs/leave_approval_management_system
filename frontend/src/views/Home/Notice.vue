<script setup lang="ts">
import useNoticeStore from '@/stores/notice';
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';

const noticeStore = useNoticeStore();

const noticeGroup = [
    {
        title: '系统通知',
        label: noticeStore.systemNotice,
    },
    {
        title: '学校通知',
        label: noticeStore.schoolNotice,
    },
    {
        title: '学院通知',
        label: noticeStore.collegeNotice,
    },
    {
        title: '辅导员通知',
        label: noticeStore.teacherNotice,
    },
];
const dailyNoticeGroup = [
    {
        icon: 'comment-o',
        title: '课程通知',
        label: '',
        route: '/notice/sign-in',
    },
    {
        icon: 'flag-o',
        title: '活动通知',
        label: '',
        route: '/notice/sign-in',
    },
];
</script>

<template>
    <div class="client-wrapper">
        <right-slide-router-view></right-slide-router-view>
        <header class="header">通知</header>
        <van-cell-group class="notice-group translucent-half" :border="false">
            <van-cell v-for="notice in noticeGroup" :title="notice.title">
                <template #label>{{ notice.label }}</template>
            </van-cell>
        </van-cell-group>
        <van-cell-group class="daily-notice translucent-half" title="日常通知" :border="false">
            <van-cell v-for="notice in dailyNoticeGroup"
                value="查看全部"
                :icon="notice.icon"
                :title="notice.title"
                :to="notice.route"
                is-link
            >
                <template #label>{{ notice.label }}</template>
            </van-cell>
        </van-cell-group>
    </div>
</template>

<style scoped lang="less">
.client-wrapper {
    padding: 20px;
    height: 100%;
    overflow-x: hidden;
    overflow-y: auto;

    .header {
        padding: 36px 18px;
        color: #fff;
        font-size: 2.2rem;
    }
    .notice-group, .daily-notice {
        .van-cell {
            :deep(.van-cell__title > span) {
                color: #4D7EE0;
                font-weight: bold;
            }
            :deep(.van-cell__value > span) {
                font-size: .8rem;
            }

            margin: 8px auto;
            border-radius: var(--van-cell-group-inset-radius);
        }
    }
}
</style>
