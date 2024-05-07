<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import type { NoticeExtra, ResponseData } from '@/utils/interface';
import { apiNoticeGet } from '@/utils/api';
import BackNavBar from '@/components/BackNavBar.vue';

const route = useRoute();
const noticeDetail = ref<NoticeExtra>()

onMounted(() => {
    apiNoticeGet(Number(route.query.id), (data: ResponseData) => {
        noticeDetail.value = data.data;
    });
});
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header" />
        <div class="view-container">
            {{ noticeDetail }}
        </div>
    </div>
</template>

<style scoped lang="less">
</style>
