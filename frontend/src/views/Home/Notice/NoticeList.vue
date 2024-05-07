<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue';
import { useRoute } from 'vue-router';
import { showSuccessToast, showFailToast } from 'vant';
import { ENoticeType, ERole, type ResponseData, type TimeRangePageQuery } from '@/utils/interface';
import { apiNoticePageQuery } from '@/utils/api/noticeApi';
import useGlobalStore from '@/stores/global';
import useUserStore from '@/stores/user';
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import BackNavBar from '@/components/BackNavBar.vue';
import NoticeCard from '@/components/NoticeCard.vue';

const route = useRoute();
const globalStore = useGlobalStore();
const userStore = useUserStore();
const query = reactive<TimeRangePageQuery & {
    _type?: number;
    userId?: number;
}>({
    pageIndex: 1,
    pageSize: 10,
    query: '',
    startDatetime: '',
    endDatetime: '',
    userId: userStore.userInfo.role === ERole.student ?
        userStore.userInfo.teacherUserId :
        userStore.userInfo.role === ERole.teacher ?
            userStore.userInfo.userId :
            undefined,
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

// 下拉刷新事件
const onRefresh = () => {
    query.pageIndex = 1;
    globalStore.noticeList.length = 0;
    getPageNotice();
};
const noticeType = <'system' | 'school' | 'college' | 'teacher'>route.path.split('/').pop();

onMounted(() => {
    switch(noticeType) {
        case 'system':
            query._type = ENoticeType.SYSTEM;
            break;
        case 'school':
            query._type = ENoticeType.SCHOOL;
            break;
        case 'college':
            query._type = ENoticeType.COLLEGE;
            break;
        case 'teacher':
            query._type = ENoticeType.TEACHER;
            break;
    }
});
</script>

<template>
    <div class="view">
        <right-slide-router-view />
        <back-nav-bar class="view-header" />
        <div class="view-container">

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
                        :state="noticeType != 'system' ? notice.state : -1"
                        :title="notice.title"
                        :content="notice.content"
                        :to="noticeType != 'system' ? `${route.path}/detail?id=${notice.id}` : ''"
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
.view-container {
    padding: 15px;
}
</style>
