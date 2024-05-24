<script setup lang="ts">
import { onMounted, reactive } from 'vue';
import { showDialog } from 'vant';
import { useRouter } from 'vue-router';
import useUserStore from '@/stores/user';
import BackNavBar from '@/components/BackNavBar.vue';
import { apiModifyPassword } from '@/utils/api';

const router = useRouter();
const userStore = useUserStore();

const modifyPasswordForm = reactive({
    password1: '',
    password2: '',
    telephone: '',
    captcha: '',
});
const modifyPasswordFormRule = {
    password1: [
        { required: true, message: '请输入密码' },
    ],
    password2: [
        { required: true, message: '请输入确认密码' },
        { validator: () => modifyPasswordForm.password1 === modifyPasswordForm.password2, message: '确认密码与密码不一致' },
    ],
    telephone: [
        { required: true, message: '请输入手机号' },
    ],
    captcha: [
        { required: true, message: '请输入验证码' },
    ],
};

const onSubmit = () => {
    apiModifyPassword({
        password: modifyPasswordForm.password1,
        captcha: modifyPasswordForm.captcha,
    });
};

onMounted(() => {
    if (!userStore.userInfo.telephone) {
        showDialog({
            title: '提示',
            message: '检测到您未绑定手机号，请先绑定手机号后再修改密码',
            confirmButtonText: '去绑定',
        }).then(() => {
            router.push('/user/modify');
        });
    }
});
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <van-form @submit="onSubmit()" required>
                <van-cell-group>
                    <van-field
                        v-model="modifyPasswordForm.password1"
                        type="password"
                        label="密码"
                        placeholder="请输入密码"
                        maxlength="16"
                        show-word-limit
                        clearable
                        label-align="top"
                        autocomplete="off"
                        :rules="modifyPasswordFormRule.password1"
                    ></van-field>
                    <van-field
                        v-model="modifyPasswordForm.password2"
                        type="password"
                        label="确认密码"
                        placeholder="请再次确认密码"
                        maxlength="16"
                        show-word-limit
                        clearable
                        label-align="top"
                        autocomplete="off"
                        :rules="modifyPasswordFormRule.password2"
                    ></van-field>
                    <van-field
                        v-model="modifyPasswordForm.telephone"
                        type="tel"
                        label="手机号码"
                        placeholder="请输入手机号"
                        maxlength="11"
                        show-word-limit
                        clearable
                        label-align="top"
                        autocomplete="off"
                        :rules="modifyPasswordFormRule.telephone"
                    ></van-field>
                    <van-field
                        v-model="modifyPasswordForm.captcha"
                        label="验证码"
                        placeholder="请输入验证码"
                        clearable
                        label-align="top"
                        autocomplete="off"
                        :rules="modifyPasswordFormRule.captcha"
                    >
                        <template #button>
                            <van-button size="small" type="primary">获取验证码</van-button>
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
