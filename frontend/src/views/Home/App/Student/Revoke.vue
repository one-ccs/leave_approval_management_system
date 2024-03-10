<script setup lang="ts">
import { ref } from 'vue';
import i18n from '@/utils/i18n';
import BackNavBar from '@/components/BackNavBar.vue';

const revokeTabsValue = ref(0);
const categoryTabsValue = ref(-1);

const revokeTabs = i18n('tabs.state.revoke');
const categoryTabs = i18n('tabs.category');
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <van-tabs class="state-tabs" v-model:active="revokeTabsValue"
                shrink
                animated
                swipeable
                lazy-render
            >
                <van-tab v-for="tab in revokeTabs"
                    title-class="tab-title"
                    :name="tab.value"
                    :title="tab.title"
                >
                    <van-empty image="search" description="暂无数据"></van-empty>
                </van-tab>
            </van-tabs>
            <van-tabs class="category-tabs" v-model:active="categoryTabsValue" shrink>
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
}
</style>
