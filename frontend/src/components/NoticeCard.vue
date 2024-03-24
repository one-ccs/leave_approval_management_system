<script setup lang="ts">
import { useRouter } from 'vue-router';

const { datetime, state, title, content, to } = defineProps({
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
    content: {
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
    <div class="notice-card">
        <div class="datetime">{{ datetime }}</div>
        <div class="card-container van-haptics-feedback" @click="router.push(to)">
            <div class="title-wrapper">
                <van-tag
                    class="state"
                    plain
                    round
                    :type="state ? 'success' : 'warning'"
                >
                    {{ state ? '已读' : '未读' }}
                </van-tag>
                <span class="title">{{ title }}</span>
                <van-icon class="icon" name="link-o"></van-icon>
            </div>
            <van-text-ellipsis rows="3" :content="content || '无'"/>
        </div>
    </div>
</template>

<style scoped lang="less">
.notice-card {
    margin: 0 auto 15px;

    .datetime {
        margin: 8px auto;
        text-align: center;
    }
    .card-container {
        border-radius: var(--border-radius);
        padding: 18px;
        background-color: #fff;
        box-shadow: var(--box-shadow-light);

        .title-wrapper {
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: flex-start;
            margin-bottom: 12px;

            .state {
                flex: 0 0 auto;
                transform: scale(1.1);
            }
            .title {
                flex: 1 0 0;
                margin-left: 18px;
                height: var(--van-tag-line-height);
                overflow: hidden;
                white-space: nowrap;
                text-overflow: ellipsis;
            }
            .icon {
                flex: 0 0 auto;
                color: #3356E4;
            }
        }
    }
}
</style>
