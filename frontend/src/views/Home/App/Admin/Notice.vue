<script setup lang="ts">
import { reactive, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { showFailToast, showSuccessToast } from 'vant';
import type { ENoticeType, ResponseData, TimeRangePageQuery } from '@/utils/interface';
import { apiNoticePageQuery } from '@/utils/api';
import useGlobalStore from '@/stores/global';
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import BackNavBar from '@/components/BackNavBar.vue';
import TimeRangeQuery from '@/components/TimeRangeQuery.vue';
import NoticeCard from '@/components/NoticeCard.vue';
import useUserStore from '@/stores/user';

const route = useRoute();
const router = useRouter();
const globalStore = useGlobalStore();
const query = reactive<TimeRangePageQuery>({
    pageIndex: 1,
    pageSize: 10,
    query: '',
    startDatetime: '',
    endDatetime: '',
});
const loading = ref(false);
const finished = ref(false);
const error = ref(false);
const refreshing = ref(false);

globalStore.noticeList.length = 0;

const getPageNotice = () => {
    loading.value = true;

    apiNoticePageQuery(query, (data: ResponseData) => {
        globalStore.noticeList.push(...data.data.list);
        finished.value = data.data.finished;
        loading.value = false;
        refreshing.value = false;
        query.pageIndex += 1;
        query.pageIndex === 2 && showSuccessToast(data.message);
    }, (data: ResponseData) => {
        refreshing.value = false;
        error.value = true;
        loading.value = false;
        showFailToast(data.message);
    });
};

// 搜索事件
const onSearch = () => {
    query.pageIndex = 1;
    getPageNotice();
};
// 下拉刷新事件
const onRefresh = () => {
    query.pageIndex = 1;
    globalStore.noticeList.length = 0;
    getPageNotice();
};
</script>

<template>
    <div class="view">
        <right-slide-router-view />
        <back-nav-bar class="view-header" right-text="发布通知" @click-right="router.push('/app/admin/notice/add')" />
        <div class="view-container">
            <time-range-query
                v-model="query"
                placeholder="请输入要查询的标题、内容"
                @search="onSearch()"
            />
            <van-pull-refresh v-model="refreshing" @refresh="onRefresh()">
                <van-list
                    class="notice-list"
                    v-model:loading="loading"
                    v-model:error="error"
                    error-text="请求失败，点击重新加载"
                    :finished="finished"
                    @load="getPageNotice()"
                >
                    <notice-card
                        v-for="notice in globalStore.noticeList"
                        :key="notice.id"
                        :datetime="notice.releaseDatetime"
                        :state="notice.state"
                        :title="notice.title"
                        :content="notice.content"
                        :to="`${route.path}/detail?id=${notice.id}`"
                    />
                    <van-back-top v-if="globalStore.noticeList.length" offset="120" bottom="56" teleport=".view-container" z-index="1"></van-back-top>
                    <template #finished>
                        <span v-if="globalStore.noticeList.length">没有更多了</span>
                        <van-empty v-else image="search" description="暂无数据" />
                    </template>
                </van-list>
            </van-pull-refresh>
        </div>
    </div>
</template>

<style scoped lang="less">
.view {
    .view-header {
        --van-nav-bar-text-color: #000;
    }
    .view-container {
        .time-range-query {
            position: sticky;
            top: 0;
            z-index: 1;
        }
        .notice-list {
            padding: 8px 15px;
        }
    }
}
</style>
