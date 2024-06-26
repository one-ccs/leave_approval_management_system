<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { showConfirmDialog, showSuccessToast } from 'vant';
import { ERole, type NoticeExtra, type ResponseData } from '@/utils/interface';
import { apiNoticeDelete, apiNoticeDetail } from '@/utils/api';
import useGlobalStore from '@/stores/global';
import BackNavBar from '@/components/BackNavBar.vue';

const route = useRoute();
const router = useRouter();
const globalStore = useGlobalStore();
const noticeId = Number(route.query.id);
const noticeDetail = ref<NoticeExtra>();

// 已读按钮点击事件
const onReadClick = () => {
    showSuccessToast('已标记为已读');
    noticeDetail.value!.state = 1;
    globalStore.noticeList.forEach(notice => {
        if (notice.id === noticeDetail.value?.id) notice.state = 1;
    });
};
// 删除按钮点击事件
const onDeleteClick = () => {
    showConfirmDialog({
        title: '提示',
        message: `确定要删除通知 "${noticeDetail.value?.title}" 吗？`,
    }).then(() => {
        apiNoticeDelete(noticeId, (data: ResponseData) => {
            showSuccessToast(data.message);
            globalStore.noticeList = globalStore.noticeList.filter(notice => notice.id !== noticeId);
            router.back();
        });
    }).catch(() => {});
};

onMounted(() => {
    apiNoticeDetail(noticeId, (data: ResponseData) => {
        noticeDetail.value = data.data;
    });
});
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <div class="head">
                <div class="title">{{ noticeDetail?.title }}</div>
                <div class="info">
                    <span class="name">{{ noticeDetail?.name }} ({{ noticeDetail?.role === ERole.admin ? '管理员' : '学校老师' }})</span>
                    <span class="release-datetime">{{ noticeDetail?.releaseDatetime }}</span>
                </div>
            </div>
            <div class="body">{{ noticeDetail?.content }}</div>
            <div class="button-group">
                <van-button
                    v-permiss="0x100"
                    class="button read"
                    type="primary"
                    round
                    plain
                    hairline
                    :disabled="!!noticeDetail?.state"
                    @click="onReadClick()"
                >已读</van-button>
                <van-button
                    v-if="$route.path.split('/')[1] === 'app'"
                    class="button delete"
                    type="danger"
                    round
                    plain
                    hairline
                    @click="onDeleteClick()"
                >删除</van-button>
            </div>
        </div>
    </div>
</template>

<style scoped lang="less">
.view {
    .view-container {
        position: unset;
        padding: var(--padding);
        background-color: #fff;

        .head {
            border-bottom: 1px solid #3333;
            padding-bottom: var(--padding);

            .title {
                margin: 8px auto var(--padding);
                font-size: 1.3rem;
            }
            .info {
                display: flex;
                color: #888;

                .release-datetime {
                    margin-left: auto;
                }
            }
        }
        .body {
            padding: 8px 0;
            line-height: 1.5rem;
        }
        .button-group {
            position: absolute;
            left: calc(var(--padding) * 2);
            bottom: var(--padding);
            width: calc(100% - var(--padding) * 4);

            .button {
                width: 100%;

                &.read {
                    background-color: #1989FA22;
                }
                &.delete {
                    background-color: #EE0A2422;
                }
            }
        }
    }
}
</style>
