<script setup lang="ts">
import { reactive } from 'vue';
import { useRouter } from 'vue-router';
import { apiLogin, type ResultData } from '@/utils/api';

const router = useRouter();
const formRules = {
    username: [
        { required: true, message: '请填写用户名' },
    ],
    password: [
        { required: true, message: '请填写密码' },
    ],
};
const formData = reactive({
    username: '',
    password: '',
    remember: false,
});

const onSubmit = (value: any) => {
    apiLogin(value, (data: ResultData) => {
        router.push('/');
    });
};
</script>

<template>
    <div class="view">
        <van-image
            block
            width="100w"
            height="380"
            fit="cover"
            position="center"
            src="static/img/img01.jpg"
            class="picture mb-5"
        ></van-image>
        <van-image src="static/img/logo.png" class="logo"></van-image>
        <van-form @submit="onSubmit" :rules="formRules">
            <van-cell-group>
                <van-field
                    v-model="formData.username"
                    name="username"
                    placeholder="请填写用户名"
                    left-icon="friends"
                    size="large"
                    clearable
                ></van-field>
                <van-field
                    v-model="formData.password"
                    name="password"
                    placeholder="请填写密码"
                    type="password"
                    left-icon="lock"
                    size="large"
                    clearable
                ></van-field>
            </van-cell-group>
            <van-cell-group inset class="d-flex align-items-center justify-content-between mt-1">
                <van-field name="remember" class="p-1 w-50">
                    <template #input>
                        <van-checkbox v-model="formData.remember" shape="square">记住密码</van-checkbox>
                    </template>
                </van-field>
                <router-link to="/forgot" class="link-button">忘记密码</router-link>
            </van-cell-group>
            <van-cell-group inset class="mt-4">
                <van-button round block type="primary" native-type="submit">登录</van-button>
            </van-cell-group>
        </van-form>
    </div>
</template>

<style scoped lang="less">
.picture {
    opacity: .8;
    max-width: var(--client-width);
    border-radius: 22% 78% 32% 68% / 67% 45% 55% 33% ;
    overflow: hidden;
}
.logo {
    z-index: 1;
    position: absolute;
    top: 35%;
    width: 256px;
}
@media screen and (min-width: 768px) {
    .logo {
        top: 28%;
    }
}
.van-form {
    width: 300px;

    :deep(.van-cell.van-cell--large) {
        border-bottom: 1px solid gray;
    }
}
</style>
