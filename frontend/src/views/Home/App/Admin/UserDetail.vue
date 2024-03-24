<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { ERole, type ResponseData, type UnionUser } from '@/utils/interface';
import { apiUserGet } from '@/utils/api';
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import BackNavBar from '@/components/BackNavBar.vue';
import Avatar from '@/components/Avatar.vue';

const route = useRoute();
const user = ref({} as UnionUser);

const getUser = () => {
    apiUserGet(Number(route.query.id), (data: ResponseData) => {
        user.value = data.data;
    });
};

onMounted(() => {
    getUser();
});
</script>

<template>
    <div class="view">
        <right-slide-router-view />
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <van-cell-group inset>
                <van-cell title="头像" is-link :to="`${route.path}/modifyAvatar?id=${route.query.id}`">
                    <template #value>
                        <!-- 加上 key 属性在头像链接改变后重新显示 -->
                        <avatar :src="user.avatar" size="66" :key="user.avatar"></avatar>
                    </template>
                </van-cell>
            </van-cell-group>

            <van-cell-group inset>
                <van-cell title="姓名" :value="user.name" />
                <van-cell title="性别" :value="user.gender" />
            </van-cell-group>

            <van-cell-group inset>
                <van-cell title="手机" :value="user.telephone" />
                <van-cell title="邮箱" :value="user.email" />
                <van-cell v-if="user.role === ERole.student" title="学号" :value="user.username" />
                <van-cell v-if="user.role === ERole.student" title="所属班级" :value="user._class" />
                <van-cell v-if="user.role === ERole.student" title="所属学部" :value="user.department" />
                <van-cell v-if="user.role === ERole.student" title="所属学院" :value="user.faculty" />
                <van-cell v-if="user.role === ERole.student" title="所属专业" :value="user.major" />
                <van-cell v-if="user.role === ERole.student" title="入学时间" :value="user.admissionDate" />

                <van-cell v-if="user.role === ERole.teacher" title="职工号" :value="user.username" />
            </van-cell-group>

            <van-cell-group v-if="user.role === ERole.student" inset>
                <van-cell title="学籍档案" is-link to="/app/student/student/record" />
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
