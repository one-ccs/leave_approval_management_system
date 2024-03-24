<script setup lang="ts">
import { useRouter } from 'vue-router';

const { datetime, state, title, describe, to } = defineProps({
    datetime: {
        type: String,
        default: 'yyyy-mm-dd HH:MM:SS',
    },
    state: {
        type: Number,
        default: 0,
    },
    title: {
        type: String,
        default: '',
    },
    describe: {
        type: String,
        default: '',
    },
    to: {
        type: String,
        default: '',
    },
});

const router = useRouter();
</script>

<template>
    <div class="sign-in-card">
        <div class="datetime">{{ datetime }}</div>
        <div class="card-container van-haptics-feedback" @click="router.push(to)">
            <van-icon class="icon" name="clock-o" size="2.8rem"></van-icon>
            <div class="content">
                <div class="title-wrapper">
                    <van-tag
                        class="state"
                        plain
                        round
                        :type="state ? 'success' : 'warning'"
                    >
                        {{ state ? '已签到' : '待签到' }}
                    </van-tag>
                    <span class="title">{{ title }}</span>
                </div>
                <div class="describe" v-if="describe">{{ describe }}</div>
            </div>
        </div>
    </div>
</template>

<style scoped lang="less">
.sign-in-card {
    margin: 0 auto 12px;

    .datetime {
        margin: 8px auto;
        text-align: center;
    }
    .card-container {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        border-radius: var(--border-radius);
        padding: 24px 18px;
        background-color: #fff;
        box-shadow: var(--box-shadow-light);

        .icon {
            opacity: .8;
        }
        .content {
            margin-left: 15px;
            max-width: calc(100% - 2.8rem - 18px);

            .title-wrapper {
                display: flex;
                flex-direction: row;
                align-items: center;
                justify-content: flex-start;
                margin-bottom: 12px;

                .state {
                    flex: 0 0 auto;
                }
                .title {
                    flex: 1 0 0;
                    margin-left: 8px;
                    height: var(--van-tag-line-height);
                    overflow: hidden;
                    white-space: nowrap;
                    text-overflow: ellipsis;
                }
            }
            .describe {
                color: #888;
                font-size: .8rem;
                overflow: hidden;
                white-space: nowrap;
                text-overflow: ellipsis;
            }
        }
    }
}
</style>
