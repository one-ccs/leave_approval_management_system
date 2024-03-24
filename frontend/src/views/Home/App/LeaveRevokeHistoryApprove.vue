<script setup lang="ts">
import { reactive, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { showFailToast, showSuccessToast } from 'vant';
import type { Leave, LeavePageQuery, ResponseData } from '@/utils/interface';
import { apiLeavePageBrief } from '@/utils/api';
import i18n from '@/utils/i18n';
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import BackNavBar from '@/components/BackNavBar.vue';
import LeaveCard from '@/components/LeaveCard.vue';

const route = useRoute();
const router = useRouter();

// 标签栏列表
const stateAllTabs = (() => {
    let result = [];
    if (String(route.name).includes('studentLeave')) {
        result = i18n('tabs.state.leave');
    }
    if (String(route.name).includes('studentRevoke')) {
        result = i18n('tabs.state.revoke');
    }
    if (String(route.name).includes('studentHistory')) {
        result = i18n('tabs.state.history');
    }
    if (String(route.name).includes('teacherApprove')) {
        result = i18n('tabs.state.approve');
    }
    return result;
})();
const categoryTabs = i18n('tabs.category');

// 跳转详情链接
const toDetail = (id: number) => {
    let result = '';
    if (String(route.name).includes('studentLeave')) {
        result = '/app/student/leave/detail?id=' + id;
    }
    if (String(route.name).includes('studentRevoke')) {
        result = '/app/student/revoke/detail?id=' + id;
    }
    if (String(route.name).includes('studentHistory')) {
        result = '/app/student/history/detail?id=' + id;
    }
    if (String(route.name).includes('teacherApprove')) {
        result = '/app/teacher/approve/detail?id=' + id;
    }
    return result;
};

// 查询参数
const query = reactive<LeavePageQuery>({
    pageIndex: 1,
    pageSize: 10,
    state: 0,
    category: -1,
});
interface LeaveExtra extends Leave {
    name: string;
}
const leaveList = reactive<LeaveExtra[]>([]);
const loading = ref(false);
const finished = ref(false);
const error = ref(false);
const refreshing = ref(false);

// 获取请假条
const getLeave = () => {
    loading.value = true;

    apiLeavePageBrief(query, (data: ResponseData) => {
        finished.value = data.data.finished;
        leaveList.push(...data.data.list);
        loading.value = false;
        refreshing.value = false;
        query.pageIndex += 1;
        showSuccessToast(data.message);
    }, (data: ResponseData) => {
        refreshing.value = false;
        error.value = true;
        loading.value = false;
        showFailToast(data.message);
    });
};
// 刷新操作
const onRefresh = () => {
    query.pageIndex = 1;
    leaveList.length = 0;
    getLeave();
};
// tab 改变操作
const onChange = () => {
    query.pageIndex = 1;
    leaveList.length = 0;
    getLeave();
};
</script>

<template>
    <div class="view">
        <right-slide-router-view />
        <back-nav-bar v-if="route.name === 'studentLeave'" class="view-header" right-text="新建申请" @click-right="router.push('/app/student/leave/add')" />
        <back-nav-bar v-else class="view-header" />
        <div class="view-container">
            <van-tabs class="state-tabs" v-model:active="query.state"
                @change="onChange()"
                shrink
                animated
                swipeable
            >
                <van-tab v-for="tab in stateAllTabs"
                    title-class="tab-title"
                    :name="tab.value"
                    :title="tab.title"
                >
                    <van-pull-refresh v-model="refreshing" @refresh="onRefresh()">
                        <van-list
                            class="leave-list"
                            v-model:loading="loading"
                            v-model:error="error"
                            error-text="请求失败，点击重新加载"
                            :finished="finished"
                            @load="getLeave()"
                        >
                            <leave-card v-for="item in leaveList" :key="item.id"
                                :id="item.id"
                                :name="item.name"
                                :state="item.state"
                                :start-datetime="item.startDatetime"
                                :end-datetime="item.endDatetime"
                                :to="toDetail(item.id)"
                            />
                            <van-back-top v-if="tab.value === query.state" offset="120" teleport=".state-tabs"></van-back-top>
                            <template #finished>
                                <span v-if="leaveList.length">没有更多了</span>
                                <van-empty v-else image="search" description="暂无数据" />
                            </template>
                        </van-list>
                    </van-pull-refresh>
                </van-tab>
            </van-tabs>
            <van-tabs class="category-tabs" v-model:active="query.category"
                @change="onChange()"
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
            :deep(.tab-title.van-tab--active) {
                .van-tab__text {
                    font-weight: bold;
                }
            }
            :deep(.van-tabs__content) {
                padding: 8px 15px;
                padding-top: calc(var(--category-tabs-height) + 8px);
                height: calc(100% - var(--van-tabs-line-height));

                .van-tab__panel {
                    height: 100%;
                    overflow-x: hidden;
                    overflow-y: auto;

                    .van-pull-refresh {
                        min-height: 100%;
                    }
                }
            }
            :deep(.van-back-top) {
                z-index: inherit;
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
