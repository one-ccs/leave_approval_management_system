<script setup lang="ts">
import { reactive, ref } from 'vue';
import { showSuccessToast } from 'vant';
import { useRouter } from 'vue-router';
import { ENoticeType, type Notice, type ResponseData } from '@/utils/interface';
import { apiNoticePut } from '@/utils/api';
import useGlobalStore from '@/stores/global';

const router = useRouter();
const globalStore = useGlobalStore();
const noticeForm = reactive({} as Notice);
const noticeFormShadow = ref({
    _type: '',
});
const categoryPickerShown = ref(false);

const noticeFormRules = {
    title: [
        { required: true, message: '请填写标题' },
    ],
    content: [
        { required: true, message: '请填写内容' },
    ],
    _type: [
        { required: true, message: '请选择通知类型' },
    ],
};
const noticeType = [
    {
        text: '系统通知',
        value: ENoticeType.SYSTEM,
    },
    {
        text: '学校通知',
        value: ENoticeType.SCHOOL,
    },
    {
        text: '学院通知',
        value: ENoticeType.COLLEGE,
    },
    {
        text: '辅导员通知',
        value: ENoticeType.TEACHER,
    },
];

// 类别选择事件
const confirmCategory = ({ selectedOptions }: any) => {
    categoryPickerShown.value = false;
    noticeForm._type = selectedOptions[0].value;
    noticeFormShadow.value._type = selectedOptions[0].text;
};
// 提交按钮点击事件
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
                        input-align="right"
                        :rules="noticeFormRules.title"
                        error-message-align="right"
                    />
                    <van-field
                        v-model="noticeForm.content"
                        label="内容"
                        placeholder="请输入内容"
                        autocomplete="off"
                        input-align="right"
                        :rules="noticeFormRules.content"
                        error-message-align="right"
                    />
                </van-cell-group>

                <van-cell-group inset>
                    <van-field
                        v-model="noticeFormShadow._type"
                        name="_type"
                        input-align="right"
                        icon-prefix="fa"
                        right-icon="caret-down"
                        clickable
                        readonly
                        label="通知类型"
                        placeholder="选择通知类型"
                        @click="categoryPickerShown = true"
                        :rules="noticeFormRules._type"
                        error-message-align="right"
                    />
                    <van-popup v-model:show="categoryPickerShown" round position="bottom">
                        <van-picker
                            :columns="noticeType"
                            @cancel="categoryPickerShown = false"
                            @confirm="confirmCategory"
                        />
                    </van-popup>
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
