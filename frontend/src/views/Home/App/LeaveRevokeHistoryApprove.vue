<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import type { Leave, LeavePageQuery, ResultData } from '@/utils/interface';
import { apiLeavePageBrief } from '@/utils/api';
import i18n from '@/utils/i18n';
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import BackNavBar from '@/components/BackNavBar.vue';
import LeaveCard from '@/components/LeaveCard.vue';
import { showFailToast, showSuccessToast } from 'vant';

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
const query = ref<LeavePageQuery>({
    pageIndex: 1,
    pageSize: 10,
    state: 0,
    category: -1,
});
interface LeaveExtra extends Leave {
    name: string;
}
const leaveList = ref<LeaveExtra[]>([]);
const loading = ref(true);

// 获取请假条
const getLeave = () => {
    apiLeavePageBrief(query.value, (data: ResultData) => {
        // 获取请假条并根据 id 升序 排序
        leaveList.value = data.data.list.sort((
            a: { id: number },
            b: { id: number },
        ) => a.id - b.id);
        loading.value = false;
        showSuccessToast(data.message);
    }, (data: ResultData) => {
        loading.value = false;
        showFailToast(data.message);
    });
};

onMounted(() => {
    getLeave();
});
</script>

<template>
    <div class="view">
        <right-slide-router-view></right-slide-router-view>
        <back-nav-bar v-if="route.name === 'studentLeave'" class="view-header" right-text="新建申请" @click-right="router.push('/app/student/leave/add')" />
        <back-nav-bar v-else class="view-header" />
        <div class="view-container">
            <van-tabs class="state-tabs" v-model:active="query.state"
                @change="getLeave()"
                shrink
                animated
                swipeable
            >
                <van-tab v-for="tab in stateAllTabs"
                    title-class="tab-title"
                    :name="tab.value"
                    :title="tab.title"
                >
                    <van-pull-refresh v-model="loading" @refresh="getLeave()">
                        <van-skeleton :loading="loading" :row="12" animate round>
                            <div class="leave-list" v-if="leaveList?.length">
                                <leave-card v-for="item in leaveList" :key="item.id"
                                    :id="item.id"
                                    :name="item.name"
                                    :state="item.state"
                                    :start-datetime="item.startDatetime"
                                    :end-datetime="item.endDatetime"
                                    :to="toDetail(item.id)"
                                />
                                <van-back-top v-if="tab.value === query.state" offset="120" teleport=".state-tabs"></van-back-top>
                            </div>
                            <van-empty v-else image="search" description="暂无数据" />
                        </van-skeleton>
                    </van-pull-refresh>
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

                    .van-skeleton {
                        --van-skeleton-paragraph-height: 103px;
                        --van-skeleton-paragraph-background: #fff;
                        --van-radius-max: 8px;
                        --van-padding-md: 0;
                    }
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