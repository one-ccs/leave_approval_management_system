<script setup lang="ts">
import useNoticeStore from '@/stores/notice';
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';

const noticeStore = useNoticeStore();

const noticeGroup = [
    {
        title: '系统通知',
        label: noticeStore.systemNotice,
        route: '/notice/system',
    },
    {
        title: '学校通知',
        label: noticeStore.schoolNotice,
        route: '/notice/school',
    },
    {
        title: '学院通知',
        label: noticeStore.collegeNotice,
        route: '/notice/college',
    },
    {
        title: '辅导员通知',
        label: noticeStore.teacherNotice,
        route: '/notice/teacher',
    },
];
const dailyNoticeGroup = [
    {
        icon: 'comment-o',
        title: '课程通知',
        label: '',
        route: '/app/student/signIn',
    },
    {
        icon: 'flag-o',
        title: '活动通知',
        label: '',
        route: '/app/student/signIn',
    },
];
</script>

<template>
    <div class="client-wrapper">
        <right-slide-router-view />
        <header class="header">通知</header>
        <van-cell-group class="notice-group translucent-half" :border="false">
            <van-cell v-for="notice in noticeGroup"
                class="van-haptics-feedback"
                :title="notice.title"
                :to="notice.route"
            >
                <template #label>{{ notice.label }}</template>
            </van-cell>
        </van-cell-group>

        <div v-permiss="0x100">
            <van-cell-group class="daily-notice translucent-half" title="日常通知" :border="false">
                <van-cell v-for="notice in dailyNoticeGroup"
                    value="查看全部"
                    :icon="notice.icon"
                    :title="notice.title"
                    :to="notice.route"
                    is-link
                    class="van-haptics-feedback"
                >
                    <template #label>{{ notice.label }}</template>
                </van-cell>
            </van-cell-group>
        </div>
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
            margin: 8px auto;
            border-radius: var(--border-radius);

            :deep(.van-cell__title > span) {
                color: #4D7EE0;
                font-weight: bold;
            }
            :deep(.van-cell__value > span) {
                font-size: .8rem;
            }
        }
        .van-cell:first-child {
            margin-top: 10px;
        }
        .van-cell:last-child {
            margin-bottom: 0;
        }
    }
    .daily-notice {
        .van-cell:first-child {
            margin-top: 0;
        }
    }
}
</style>
