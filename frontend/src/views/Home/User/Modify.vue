<script setup lang="ts">
import useUserStore from '@/stores/user';
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import BackNavBar from '@/components/BackNavBar.vue';
import Avatar from '@/components/Avatar.vue';

const userStore = useUserStore();
</script>

<template>
    <div class="view">
        <right-slide-router-view />
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <van-cell-group inset>
                <van-cell title="头像" is-link to="/user/modify/avatar">
                    <template #value>
                        <avatar :src="userStore.userInfo.avatar" size="66"></avatar>
                    </template>
                </van-cell>
            </van-cell-group>

            <van-cell-group inset>
                <van-cell title="姓名" :value="userStore.userInfo.name" />
                <van-cell title="性别" :value="userStore.userInfo.gender" />
            </van-cell-group>

            <van-cell-group inset>
                <van-cell title="手机" label="修改或绑定手机号" is-link to="/user/modify/telephone"></van-cell>
                <van-cell title="邮箱" :value="userStore.userInfo.email" />
                <van-cell v-permiss="0x100" title="学号" :value="userStore.userInfo.username" />
                <van-cell v-permiss="0x100" title="所属班级" :value="userStore.userInfo._class" />
                <van-cell v-permiss="0x100" title="所属学部" :value="userStore.userInfo.department" />
                <van-cell v-permiss="0x100" title="所属学院" :value="userStore.userInfo.faculty" />
                <van-cell v-permiss="0x100" title="所属专业" :value="userStore.userInfo.major" />
                <van-cell v-permiss="0x100" title="入学时间" :value="userStore.userInfo.admissionDate" />
                <van-cell v-permiss="0x100" title="学籍状态" value="正常" />
                <van-cell v-permiss="0x100" title="国际化项目" value="无留学" />

                <van-cell v-permiss="0x200" title="职工号" :value="userStore.userInfo.username" />
            </van-cell-group>
        </div>
    </div>
</template>

<style scoped lang="less">
.view-container {
    .van-cell-group {
        margin-top: 16px;
    }
}
</style>
