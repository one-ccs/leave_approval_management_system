<script setup lang="ts">
import { useRouter } from 'vue-router';
import { useStateColor } from '@/utils/use';
import i18n from '@/utils/i18n';
import useUserStore from '@/stores/user';

const { id, state, startDatetime, endDatetime, to } = defineProps({
    id: {
        type: Number,
        required: true,
    },
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
    to: {
        type: String,
        required: true,
    }
});

const router = useRouter();
const userStore = useUserStore();
</script>

<template>
    <div class="leave-card van-haptics-feedback" @click="router.push({ path: to, query: { id } })">
        <div class="icon-wrapper" :style="{ color: useStateColor(state) }">
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
    border-radius: var(--border-radius);
    padding: 24px;
    width: 100%;
    background: #fff;

    .icon-wrapper {
        flex: 0 1 auto;
        text-align: center;

        .text {
            margin-top: 5px;
            font-size: .8rem;
        }
    }
    .info-wrapper {
        flex: 1 0 auto;
        margin-left: 24px;

        .title {
            margin-bottom: 8px;
            font-size: 1rem;
            font-weight: bold;
        }
        .datetime {
            margin: 3px auto;
            color: #888;
            font-size: .8rem;
        }
        .datetime:first-child {
            margin-top: 0;
        }
        .datetime:last-child {
            margin-bottom: 0;
        }
    }
    .angle-right {
        color: #888;
    }
}
</style>
