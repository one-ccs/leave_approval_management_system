<script setup lang="ts">
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router';
import type { ResponseData } from '@/utils/interface';
import { apiLogin } from '@/utils/api';
import useGlobalStore from '@/stores/global';
import useUserStore from '@/stores/user';

const router = useRouter();
const globalStore = useGlobalStore();
const userStore = useUserStore();
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
const passwordInputRef = ref();

const onSubmit = (value: any) => {
    apiLogin(value, (data: ResponseData) => {
        userStore.clear().setUser(data.data).save();
        router.push('/');
    });
};
</script>

<template>
    <div class="view">
        <div class="logo-box">
            <van-image
                class="picture"
                block
                width="100w"
                height="380"
                fit="cover"
                position="center"
                src="static/img/img01.jpg"
            ></van-image>
            <van-image src="static/img/logo.png" class="logo"></van-image>
        </div>
        <van-form @submit="onSubmit">
            <van-cell-group class="translucent">
                <van-field
                    v-model="formData.username"
                    name="username"
                    placeholder="请填写用户名"
                    left-icon="friends"
                    size="large"
                    clearable
                    :rules="formRules.username"
                    @keypress.enter="passwordInputRef.focus()"
                ></van-field>
                <van-field
                    ref="passwordInputRef"
                    v-model="formData.password"
                    name="password"
                    placeholder="请填写密码"
                    type="password"
                    left-icon="lock"
                    size="large"
                    clearable
                    :rules="formRules.password"
                ></van-field>
            </van-cell-group>
            <van-cell-group inset class="d-flex align-items-center justify-content-between mt-1 translucent">
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
        <div class="test-accounts">
            <span>测试账号：</span>
            <div class="account">角色：管理员，用户名：1202，密码：903</div>
            <div class="account">角色：辅导员，用户名：100000，密码：123</div>
            <div class="account">角色：学生，用户名：2000000000，密码：123</div>
        </div>
        <div class="copyright">
            <span class="version">版本：{{ globalStore.version }}</span>
            <van-divider vertical></van-divider>
            <span class="accord">隐私政策和服务协议</span>
        </div>
    </div>
</template>

<style scoped lang="less">
.view {
    .logo-box {
        position: relative;
        margin-bottom: 3rem;

        .picture {
            opacity: .8;
            max-width: var(--client-width);
            border-radius: 22% 78% 32% 68% / 67% 45% 55% 33% ;
            overflow: hidden;
        }
        .logo {
            z-index: 1;
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 256px;
        }
    }
    .van-form {
        width: 300px;

        :deep(.van-cell.van-cell--large) {
            border-bottom: 1px solid gray;
        }
    }
    .test-accounts {
        margin-top: 1.5rem;
        font-size: .8rem;
        color: #888;
    }
    .copyright {
        margin-top: auto;
        margin-bottom: 8px;
        color: #333;
        font-size: .66rem;

        .version {
            margin-left: 8px;
        }
    }
}
</style>
