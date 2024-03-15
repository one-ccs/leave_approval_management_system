<script setup lang="ts">
import i18n from '@/utils/i18n';
import useUserStore from '@/stores/user';
import { LeaveState } from '@/utils/interface';

const { state, startDatetime, endDatetime } = defineProps({
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

const iconColor = () => {
    switch(state){
        case LeaveState.PENDING:
            return '#c2c2c2';
        case LeaveState.WITHDRAWN:
            return '#c2c2c2';
        case LeaveState.REJECTED:
            return '#ff8383';
        case LeaveState.CANCEL:
            return '#345';
        case LeaveState.CANCELING:
            return '#345';
        case LeaveState.DONE:
            return '#6dd080';
    }
};
</script>

<template>
    <div class="leave-card">
        <div class="icon-wrapper" :style="{ color: iconColor() }">
            <van-icon name="notes-o" size="38"></van-icon>
            <div class="text">{{ i18n(state, 'field.leave.state') }}</div>
        </div>
        <div class="info-wrapper">
            <div class="title">{{ userStore.userInfo.name }}的请假申请</div>
            <div class="datetime">开始时间：{{ startDatetime }}</div>
            <div class="datetime">结束时间：{{ endDatetime }}</div>
        </div>
        <div class="angle-right">
            <van-icon class-prefix="fa" name="angle-right"></van-icon>
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
    padding: 18px;
    width: 100%;
    background: #fff;

    .icon-wrapper {
        flex: 0 1 auto;
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
            margin-bottom: 8px;
            font-size: 1.15rem;
            font-weight: bold;
        }
        .datetime {
            margin: 3px auto;
            color: #888;
            font-size: .9rem;
        }
    }
    .angle-right {
        color: #888;
    }
}
</style>
