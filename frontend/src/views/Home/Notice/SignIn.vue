<script setup lang="ts">
import { ref } from 'vue';
import BackNavBar from '@/components/BackNavBar.vue';
import useUserStore from '@/stores/user';

const userStore = useUserStore();
const notices = ref([
    {
        datetime: '2024-3-5 21:53:41',
        state: 0,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 1,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 0,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 0,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 1,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 1,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 0,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 1,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 1,
        title: '查寝',
    },
    {
        datetime: '2024-3-5 22:11:52',
        state: 1,
        title: '查寝',
    },
]);
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header"></back-nav-bar>
        <div class="view-container">
            <div class="notice-list">
                <div class="notice-item" v-for="notice in notices">
                    <div class="notice-datetime">{{ notice.datetime }}</div>
                    <div class="notice-card">
                        <van-icon class="notice-icon" name="clock-o" size="2.8rem"></van-icon>
                        <div class="notice-content">
                            <div class="notice-title">
                                <van-button
                                    class="state"
                                    plain
                                    round
                                    tag="div"
                                    size="mini"
                                    :type="notice.state ? 'success' : 'warning'"
                                    :text="notice.state ? '已签到' : '待签到'"
                                ></van-button>
                                <div class="title">{{ notice.title }}</div>
                            </div>
                            <div class="notice-describe">{{ userStore.userInfo.major }}</div>
                        </div>
                    </div>
                </div>
            </div>
            <van-back-top></van-back-top>
        </div>
    </div>
</template>

<style scoped lang="less">
.view {
    .view-container {

        .notice-list {
            margin: 0 15px;

            .notice-item {
                margin: 8px auto;

                .notice-datetime {
                    margin: 8px auto;
                    text-align: center;
                }
                .notice-card {
                    display: flex;
                    flex-direction: row;
                    align-items: center;
                    justify-content: flex-start;
                    border-radius: 8px;
                    padding: 24px 18px;
                    background-color: #fff;

                    .notice-icon {
                        opacity: .8;
                        margin-right: 18px;
                    }
                    .notice-content {
                        .notice-title {
                            display: flex;
                            flex-direction: row;
                            align-items: center;
                            justify-content: flex-start;
                            margin-bottom: 8px;

                            .state {
                                margin-right: 8px;
                            }
                        }
                        .notice-describe {
                            color: #888;
                            font-size: .8rem;
                        }
                    }
                }
            }
        }
    }
}
</style>
