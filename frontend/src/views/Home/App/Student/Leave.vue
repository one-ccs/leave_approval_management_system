<script setup lang="ts">
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import BackNavBar from '@/components/BackNavBar.vue';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const router = useRouter();
const stateTabsValue = ref(0);
const categoryTabsValue = ref(0);

const stateTabs = [
    {
        title: '待审批',
        state: 0,
    },
    {
        title: '已撤回',
        state: 1,
    },
    {
        title: '已驳回',
        state: 2,
    },
    {
        title: '已完成',
        state: 3,
    },
];
const categoryTabs = [
    {
        title: '全部类型',
        category: 0,
    },
    {
        title: '事假',
        category: 1,
    },
    {
        title: '病假',
        category: 2,
    },
    {
        title: '公假',
        category: 3,
    },
    {
        title: '出校申请',
        category: 4,
    },
];
</script>

<template>
    <div class="view">
        <right-slide-router-view></right-slide-router-view>
        <back-nav-bar class="view-header" right-text="新建申请" @click-right="router.push('/app/student/leave/add')"></back-nav-bar>
        <div class="view-container">
            <van-tabs class="state-tabs" v-model:active="stateTabsValue"
                shrink
                animated
                swipeable
                lazy-render
            >
                <van-tab v-for="tab in stateTabs"
                    title-class="tab-title"
                    :name="tab.state"
                    :title="tab.title"
                >
                    {{ tab.title }}
                </van-tab>
            </van-tabs>
            <van-tabs class="category-tabs" v-model:active="categoryTabsValue"
                shrink
            >
                <van-tab v-for="tab in categoryTabs"
                    title-class="tab-title"
                    :name="tab.category"
                    :title="tab.title"
                ></van-tab>
            </van-tabs>
        </div>
    </div>
</template>

<style scoped lang="less">
.view-container {
    --category-tabs-height: 30px;
    position: relative;

    --van-tabs-line-height: 38px;

    .state-tabs {
        position: relative;
        width: 100%;
        height: 100%;

        :deep([role="tablist"]) {
            padding: 0 0 10px 0;
            background-color: #fff;

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
            padding: 8px;
            padding-top: calc(var(--category-tabs-height) + 8px);
            height: calc(100% - var(--van-tabs-line-height));
        }
    }
    .category-tabs {
        position: absolute;
        top: var(--van-tabs-line-height);
        left: 0;
        width: 100%;

        :deep([role="tablist"]) {
            padding: 0 0 10px 0;
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
</style>
