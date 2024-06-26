<script setup lang="ts">
import { useRouter } from 'vue-router';
import { ERole, type UnionUser } from '@/utils/interface';
import Avatar from './Avatar.vue';

const { user, to } = defineProps({
    user: {
        type: Object as () => UnionUser,
        required: true,
    },
    to: {
        type: String,
        required: true,
    },
});

const router = useRouter();
</script>

<template>
    <div class="user-card van-haptics-feedback" @click="router.push(to)">
        <avatar :src="user.avatar" size="50" loading-size="24"></avatar>
        <div class="info-wrapper" v-if="user.role === ERole.student">
            <div class="info-item">
                <span class="label">学号</span>
                <span class="text">：{{ user.username }}</span>
            </div>
            <div class="info-item">
                <span class="label">姓名</span>
                <span class="text">：{{ user.name }}</span>
            </div>
            <div class="info-item">
                <span class="label">辅导员</span>
                <span class="text">：{{ user.assistantName }}</span>
            </div>
            <div class="info-item">
                <span class="label">班级</span>
                <span class="text">：{{ `${user.grade}${user.major}${user._class}班` }}</span>
            </div>
        </div>
        <div class="info-wrapper" v-if="user.role === ERole.assistant">
            <div class="info-item">
                <span class="label">职工号</span>
                <span class="text">：{{ user.username }}</span>
            </div>
            <div class="info-item">
                <span class="label">姓名</span>
                <span class="text">：{{ user.name }}</span>
            </div>
            <div class="info-item">
                <span class="label">联系方式</span>
                <span class="text">：{{ user.telephone || '/' }}</span>
            </div>
        </div>
        <div class="info-wrapper" v-if="user.role === ERole.admin">
            <div class="info-item">
                <span class="label">用户名</span>
                <span class="text">：{{ user.username }}</span>
            </div>
            <div class="info-item">
                <span class="label">姓名</span>
                <span class="text">：{{ user.name }}</span>
            </div>
            <div class="info-item">
                <span class="label">联系方式</span>
                <span class="text">：{{ user.telephone || '/' }}</span>
            </div>
        </div>
        <div class="angle-right">
            <van-icon class-prefix="fa" name="angle-right"></van-icon>
        </div>
    </div>
</template>

<style scoped lang="less">
.user-card {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    margin: 8px auto 0;
    border-radius: var(--border-radius);
    padding: 15px;
    width: 100%;
    font-size: .95rem;
    background: #fff;
    box-shadow: var(--box-shadow-light-2);

    .info-wrapper {
        flex: 1 0 auto;
        margin-left: 15px;
        max-width: calc(100% - 15px - 50px - 16px);

        .info-item {
            margin-bottom: 3px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;

            .label {
                display: inline-block;
                width: 3.8rem;
                text-align: justify;
                text-align-last: justify;
                white-space: nowrap;
            }
            .text {
                overflow: hidden;
                white-space: nowrap;
                text-overflow: ellipsis;
            }
        }
        .info-item:last-child {
            margin-bottom: 0;
        }
    }
    .angle-right {
        flex: 0 0 auto;
        color: #888;
    }
}
.user-card:first-child {
    margin-top: 0;
}
</style>
