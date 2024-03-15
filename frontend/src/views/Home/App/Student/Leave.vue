<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import type { Leave, LeavePageQuery, ResultData } from '@/utils/interface';
import { apiLeavePageBrief } from '@/utils/api';
import i18n from '@/utils/i18n';
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import BackNavBar from '@/components/BackNavBar.vue';
import LeaveCard from '@/components/LeaveCard.vue';

const router = useRouter();

// 标签栏列表
const stateTabs = i18n('tabs.state.leave');
const categoryTabs = i18n('tabs.category');

// 查询参数
const query = ref<LeavePageQuery>({
    pageIndex: 1,
    pageSize: 10,
    state: 0,
    category: -1,
});
const leaveList = ref<Leave[]>([]);

// 获取请假条
const getLeave = () => {
    apiLeavePageBrief(query.value, (data: ResultData) => {
        leaveList.value = data.data.list;
    });
};

onMounted(() => {
    getLeave();
});
</script>

<template>
    <div class="view">
        <right-slide-router-view></right-slide-router-view>
        <back-nav-bar class="view-header" right-text="新建申请" @click-right="router.push('/app/student/leave/add')"></back-nav-bar>
        <div class="view-container">
            <van-tabs class="state-tabs" v-model:active="query.state"
                @change="getLeave()"
                shrink
                animated
                swipeable
                lazy-render
            >
                <van-tab v-for="tab in stateTabs"
                    title-class="tab-title"
                    :name="tab.value"
                    :title="tab.title"
                >
                    <div class="leave-list" v-if="leaveList?.length">
                        <leave-card v-for="item in leaveList"
                            :key="item.id"
                            :id="item.id"
                            :state="item.state"
                            :start-datetime="item.startDatetime"
                            :end-datetime="item.endDatetime"
                            to="/app/student/leave/detail"
                        />
                        <van-back-top></van-back-top>
                    </div>
                    <van-empty v-else image="search" description="暂无数据" />
                </van-tab>
            </van-tabs>
            <van-tabs class="category-tabs" v-model:active="query.category"
                @change="getLeave()"
                shrink
            >
                <van-tab v-for="tab in categoryTabs"
                    title-class="tab-title"
                    :name="tab.value"
                    :title="tab.title"
                ></van-tab>
            </van-tabs>
        </div>
    </div>
</template>

<style scoped lang="less">
.view {
    .view-header {
        --van-nav-bar-text-color: #000;
    }
    .view-container {
        --category-tabs-height: 30px;
        position: relative;

        --van-tabs-line-height: 38px;

        .state-tabs {
            position: relative;
            width: 100%;
            height: 100%;

            :deep([role="tablist"]) {
                padding: 0;
                padding-left: 3px;

                .van-tabs__line {
                    display: none;
                }
            }
            :deep(.tab-title) {
                font-size: .85rem;
            }
            :deep(.tab-title.van-tab--active .van-tab__text) {
                font-weight: bold;
            }
            :deep(.van-tabs__content) {
                padding: 8px 15px;
                padding-top: calc(var(--category-tabs-height) + 8px);
                height: calc(100% - var(--van-tabs-line-height));

                .van-tab__panel {
                    height: 100%;
                    overflow-x: hidden;
                    overflow-y: auto;
                }
            }
        }
        .category-tabs {
            position: absolute;
            top: var(--van-tabs-line-height);
            left: 0;
            width: 100%;

            :deep([role="tablist"]) {
                padding: 0;
                background-color: #fff;

                .van-tabs__line {
                    display: none;
                }
            }
            :deep(.van-tabs__wrap) {
                height: var(--category-tabs-height);
            }
            :deep(.tab-title) {
                font-size: .8rem;
            }
            :deep(.tab-title.van-tab--active .van-tab__text) {
                border-radius: 12px;
                padding: 0 8px;
                color: #fff;
                background-color: #29B9FD;
            }
        }
    }
}
</style>
