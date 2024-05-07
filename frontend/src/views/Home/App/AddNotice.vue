<script setup lang="ts">
import { reactive } from 'vue';
import { showSuccessToast } from 'vant';
import { useRouter } from 'vue-router';
import type { Notice, ResponseData } from '@/utils/interface';
import { apiNoticePut } from '@/utils/api';
import useGlobalStore from '@/stores/global';

const router = useRouter();
const globalStore = useGlobalStore();
const noticeForm = reactive({} as Notice);

const noticeFormRules = {
    title: [
        { required: true, message: '请填写标题' },
    ],
    content: [
        { required: true, message: '请填写内容' },
    ],
};

const onSubmit = () => {
    apiNoticePut(noticeForm, (data: ResponseData) => {
        showSuccessToast(data.message);
        globalStore.noticeList.push(data.data);
        router.back();
    });
};
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <van-form @submit="onSubmit()" required>
                <van-cell-group inset>
                    <van-field
                        v-model="noticeForm.title"
                        label="标题"
                        placeholder="请输入标题"
                        autocomplete="off"
                        :rules="noticeFormRules.title"
                    />
                    <van-field
                        v-model="noticeForm.content"
                        label="内容"
                        placeholder="请输入内容"
                        autocomplete="off"
                        :rules="noticeFormRules.content"
                    />
                </van-cell-group>

                <van-cell-group inset class="button-group transparent">
                    <van-button round block type="primary" native-type="submit">提交</van-button>
                </van-cell-group>
            </van-form>
        </div>
    </div>
</template>

<style scoped lang="less">
.view-container {
    .van-form {

        .van-cell-group {
            margin-top: 15px;
        }
        .button-group {
            position: sticky;
            bottom: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 0 16px;
        }
    }
}
</style>
