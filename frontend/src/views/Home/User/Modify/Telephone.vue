<script setup lang="ts">
import { reactive, ref } from 'vue';
import BackNavBar from '@/components/BackNavBar.vue';
import { apiModifyTelephone } from '@/utils/api';
import { showSuccessToast } from 'vant';
import type { ResponseData } from '@/utils/interface';
import useUserStore from '@/stores/user';


const userStore = useUserStore();
const modifyTelephoneForm = reactive({
    telephone: '',
    captcha: '',
});
const modifyTelephoneFormRules = {
    telephone: [
        { required: true, message: '请输入手机号' },
    ],
    captcha: [
        { required: true, message: '请输入验证码' },
    ],
};
const btnCaptchaDisabled = ref(false);
const btnCaptchaText = ref('获取验证码');

let timer: number;
const onCaptchaClick = () => {
    btnCaptchaDisabled.value = true;
    btnCaptchaText.value = '重新获取(60)';

    let i = 59;
    timer = setInterval(() => {
        btnCaptchaText.value = `重新获取(${i--})`;
        if (i <= 0) {
            clearInterval(timer);
            i = 60;
            btnCaptchaDisabled.value = false;
        }
    }, 1000);
};
const onSubmit = () => {
    apiModifyTelephone(modifyTelephoneForm, (data: ResponseData) => {
        showSuccessToast(data.message);
        userStore.userInfo.telephone = modifyTelephoneForm.telephone;
    });
};
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <van-form @submit="onSubmit()" required>
                <van-cell-group>
                    <van-field
                        v-model="modifyTelephoneForm.telephone"
                        type="tel"
                        label="手机号码"
                        placeholder="请输入手机号"
                        maxlength="11"
                        show-word-limit
                        clearable
                        label-align="top"
                        autocomplete="off"
                        :rules="modifyTelephoneFormRules.telephone"
                    ></van-field>
                    <van-field
                        v-model="modifyTelephoneForm.captcha"
                        label="验证码"
                        placeholder="请输入验证码"
                        clearable
                        label-align="top"
                        autocomplete="off"
                        :rules="modifyTelephoneFormRules.captcha"
                    >
                        <template #button>
                            <van-button :disabled="btnCaptchaDisabled" size="small" type="primary" @click="onCaptchaClick()">{{ btnCaptchaText }}</van-button>
                        </template>
                    </van-field>
                </van-cell-group>

                <div class="btn-submit">
                    <van-button round block type="primary" native-type="submit">提交</van-button>
                </div>
            </van-form>
        </div>
    </div>
</template>

<style scoped lang="less">
.view {
    .view-container {
        padding: var(--padding);

        .van-form {
            .van-cell-group {
                border-radius: var(--border-radius);
                overflow: hidden;
            }
            .btn-submit {
                margin: var(--padding) calc(var(--padding) * 2) 0;
            }
        }
    }
}
</style>
