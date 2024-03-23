<script setup lang="ts">
import { reactive, ref, onMounted } from 'vue';
import type { User, ResultData, UserPageQuery } from '@/utils/interface';
import { apiUserPageQuery } from '@/utils/api';
import BackNavBar from '@/components/BackNavBar.vue';
import UserCard from '@/components/UserCard.vue';

const query = reactive<UserPageQuery>({
    pageIndex: 0,
    pageSize: 10,
    query: '',
    startDatetime: '',
    endDatetime: '',
});
const total = ref(0);
const userList = reactive<User[]>([]);

const getPageUser = () => {
    apiUserPageQuery(query, (data: ResultData) => {

        console.log(data);
    });
};
const onPageSizeChange = (n: number) => {

console.log(n);
};

onMounted(() => {
    getPageUser();
});
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <template v-if="userList.length">
                <user-card></user-card>
                <van-pagination
                    v-model="query.pageIndex"
                    :items-per-page="query.pageSize"
                    :total-items="total"
                    :show-page-size="5"
                    force-ellipses
                    @change="onPageSizeChange"
                />
            </template>
            <van-empty v-else image="search" description="暂无数据" />
        </div>
    </div>
</template>

<style scoped lang="less">
</style>
