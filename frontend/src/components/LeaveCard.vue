<script setup lang="ts">
import i18n from '@/utils/i18n';
import useUserStore from '@/stores/user';

const { startDatetime, endDatetime } = defineProps({
    state: {
        type: Number,
        required: true,
    },
    startDatetime: {
        type: String,
        required: true,
    },
    endDatetime: {
        type: String,
        required: true,
    },
});

const userStore = useUserStore();
</script>

<template>
    <div class="leave-card">
        <div class="icon-wrapper">
            <van-icon name="notes-o" size="36"></van-icon>
            <div class="text">{{ i18n(state, 'field.leave.state') }}</div>
        </div>
        <div class="info-wrapper">
            <div class="title">{{ userStore.userInfo.name }}的请假申请</div>
            <div class="start-datetime">开始时间：{{ startDatetime }}</div>
            <div class="end-datetime">结束时间：{{ endDatetime }}</div>
        </div>
    </div>
</template>

<style scoped lang="less">
.leave-card {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    margin: 8px auto;
    border-radius: 8px;
    padding: 18px 36px;
    width: 100%;
    background: #0005;

    .icon-wrapper {
        flex: 0 0 20%;
        background: #0f0;
        text-align: center;

        .text {
            margin-top: 5px;
            font-size: .85rem;
        }
    }
    .info-wrapper {
        flex: 1 0 auto;
        margin-left: 24px;

        .title {
            margin-bottom: 5px;
            font-size: 1.25rem;
            font-weight: bold;
        }
    }
}
</style>
