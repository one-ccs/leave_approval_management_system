<script setup lang="ts">
import { onMounted, reactive } from 'vue';
import { showDialog } from 'vant';
import { useRouter } from 'vue-router';
import useUserStore from '@/stores/user';
import BackNavBar from '@/components/BackNavBar.vue';

const router = useRouter();
const userStore = useUserStore();

const modifyPasswordForm = reactive({
    telephone: '',
    captcha: '',
});

const onSubmit = () => {

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
            <van-form @submit="onSubmit()">
                <van-cell-group inset>
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
                    ></van-field>
                    <van-field
                        v-model="modifyPasswordForm.captcha"
                        label="验证码"
                        placeholder="请输入验证码"
                        clearable
                        label-align="top"
                        autocomplete="off"
                    >
                        <template #button>
                            <van-button size="small" type="primary">获取验证码</van-button>
                        </template>
                    </van-field>
                </van-cell-group>
            </van-form>
        </div>
    </div>
</template>

<style scoped lang="less">
.view-container {
    margin-top: 16px;
}
</style>
