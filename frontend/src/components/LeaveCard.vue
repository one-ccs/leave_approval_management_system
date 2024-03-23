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
    name: {
        type: String,
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
    <div class="leave-card van-haptics-feedback" @click="router.push(to)">
        <div class="icon-wrapper" :style="{ color: useStateColor(state) }">
            <van-icon name="notes-o" size="38"></van-icon>
            <div class="text">{{ i18n(state, 'field.leave.state') }}</div>
        </div>
        <div class="info-wrapper">
            <div class="title">
                <div class="text">{{ name }}的请假申请</div>
                <div class="no">(No.{{ id }})</div>
            </div>
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
    box-shadow: 0 2px 5px 0 #3333;

    .icon-wrapper {
        flex: 0 1 auto;
        text-align: center;

        .text {
            margin-top: 5px;
            font-size: .8rem;
        }
    }
    .info-wrapper {
        flex: 1 1 auto;
        flex-basis: 30%;
        margin-left: 24px;
        max-width: calc(100% - 24px - 38px - 16px);

        .title {
            display: flex;
            align-items: center;
            justify-content: flex-start;
            margin-bottom: 9px;

            .text {
                font-size: 1rem;
                font-weight: bold;
                overflow: hidden;
                white-space: nowrap;
                text-overflow: ellipsis;
            }
            .no {
                margin-left: 5px;
                font-size: .8rem;
                white-space: nowrap;
            }
        }
        .datetime {
            margin: 5px auto;
            color: #888;
            font-size: .8rem;
        }
        .datetime:nth-last-child(2) {
            margin-top: 0;
        }
        .datetime:last-child {
            margin-bottom: 0;
        }
    }
    .angle-right {
        flex: 0 0 auto;
        color: #888;
    }
}
</style>
