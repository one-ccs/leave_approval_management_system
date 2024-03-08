<script setup lang="ts">
import { showSuccessToast, type ButtonType, showFailToast } from 'vant';
import { useRouter } from 'vue-router';
import { apiLogout, type ResultData } from '@/utils/api';
import useUserStore from '@/stores/user';
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import useGlobalStore from '@/stores/global';

const router = useRouter();
const globalStore = useGlobalStore();
const userStore = useUserStore();

const checkUpdate =() => {
    showSuccessToast("最新版本");
};
const logout = () => {
    apiLogout();
    userStore.clear();
    router.replace({ name: 'login'});
};

const iconPrefix= 'fa';
const cells = [
    {
        icon: 'edit',
        title: '编辑资料',
        route: '/user/modify',
    },
    {
        icon: 'lock',
        title: '修改密码',
        route: '/user/password',
    },
    {
        icon: 'gear',
        title: '设置',
        route: '/user/setting',
    },
];
const buttons = [
    {
        icon: 'rocket',
        text: '检查更新',
        type: 'primary',
        dot: globalStore.isUpdate,
        onClick: checkUpdate,
    },
    {
        icon: 'sign-out',
        text: '退出登录',
        type: 'danger',
        dot: false,
        onClick: logout,
    },
];
</script>

<template>
    <div class="client-wrapper">
        <right-slide-router-view></right-slide-router-view>
        <div class="user-card">
            <van-image class="avatar" :src="userStore.userInfo.avatar" round width="88" height="88"></van-image>
            <van-space class="info" direction="vertical" :size="5">
                <div class="name">{{ userStore.userInfo.name }}</div>
                <div class="role">{{ userStore.userInfo.role }}</div>
                <div class="major">{{ userStore.userInfo.major }}</div>
            </van-space>
        </div>
        <van-cell-group class="cell-group">
            <van-cell v-for="cell in cells" :key="cell.route"
                size="large"
                :icon-prefix="iconPrefix"
                :icon="cell.icon"
                :title="cell.title"
                :to="cell.route"
                is-link
            ></van-cell>
        </van-cell-group>
        <van-space class="button-group" direction="vertical" :size="8" fill>
            <van-button v-for="button in buttons" :key="button.icon"
                round
                block
                icon-position="right"
                :type="(button.type as ButtonType)"
                :text="button.text"
                @click="button.onClick()"
            >
                <template #icon>
                    <van-icon :class-prefix="iconPrefix" :name="button.icon" :dot="button.dot"></van-icon>
                </template>
            </van-button>
        </van-space>
    </div>
</template>

<style scoped lang="less">
.client-wrapper {
    padding: 20px;
    height: 100%;
    overflow-x: hidden;
    overflow-y: auto;

    .user-card {
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        align-items: center;
        justify-content: flex-start;
        margin: 50px 0;
        border-radius: 8px;
        padding: 15px 0;
        background-color: #fffa;

        .avatar {
            margin: 0 15px;
        }
        .name {
            font-size: 1.3rem;
        }
        .role, .major {
            color: #333;
            font-size: .8rem;
        }
    }
    .cell-group {
        --van-cell-group-background: #0000;
        --van-cell-background: #fffa;
        border-radius: var(--van-cell-group-inset-radius);
        overflow: hidden;
    }
    .button-group {
        opacity: .85;
        position: sticky;
        top: 888%;
        margin: 20px auto;
        padding: 0 20px;
        width: 75%;
    }
}
</style>
