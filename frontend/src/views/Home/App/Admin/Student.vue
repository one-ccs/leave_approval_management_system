<script setup lang="ts">
import { reactive, ref, onMounted } from 'vue';
import type { ResponseData, TimeRangePageQuery, UnionUser } from '@/utils/interface';
import { apiStudentPageQuery } from '@/utils/api';
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import BackNavBar from '@/components/BackNavBar.vue';
import TimeRangeQuery from '@/components/TimeRangeQuery.vue';
import UserCard from '@/components/UserCard.vue';

const query = reactive<TimeRangePageQuery>({
    pageIndex: 1,
    pageSize: 30,
    query: '',
    startDatetime: '',
    endDatetime: '',
});
const total = ref(0);
const userList = reactive<UnionUser[]>([]);

// 分页查询用户
const getPageUser = () => {
    apiStudentPageQuery(query, (data: ResponseData) => {
        total.value = data.data.total;
        userList.length = 0;
        userList.push(...data.data.list);
    });
};
// 搜索事件
const onSearch = () => {
    query.pageIndex = 1;
    getPageUser();
};

onMounted(() => {
    getPageUser();
});
</script>

<template>
    <div class="view">
        <right-slide-router-view />
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <time-range-query
                class="time-range-query"
                v-model="query"
                @search="onSearch()"
            />
            <div v-if="userList.length" class="container">
                <div class="user-list">
                    <user-card v-for="user in userList" :key="user.id"
                        :user="user"
                        :to="`/app/admin/student/detail?id=${user.id}`"
                    />
                    <van-back-top offset="120" bottom="56" teleport=".view-container" z-index="1"></van-back-top>
                </div>
                <van-pagination
                    class="van-safe-area-bottom"
                    v-model="query.pageIndex"
                    :items-per-page="query.pageSize"
                    :total-items="total"
                    :show-page-size="5"
                    force-ellipses
                    @change="getPageUser()"
                />
            </div>
            <van-empty v-else image="search" description="暂无数据" />
        </div>
    </div>
</template>

<style scoped lang="less">
.view-container {
    .time-range-query {
        position: sticky;
        top: 0;
        z-index: 1;
    }
    .container {
        .user-list {
            padding: 15px;
        }
        .van-pagination {
            z-index: 1;
            position: sticky;
            bottom: 0;
        }
    }
}
</style>
