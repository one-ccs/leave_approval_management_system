<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { LeaveState, type Leave, type ResultData } from '@/utils/interface';
import { apiLeaveGet } from '@/utils/api';
import { useLeaveDuration, useStateColor } from '@/utils/use';
import i18n from '@/utils/i18n';
import useUserStore from '@/stores/user';
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import BackNavBar from '@/components/BackNavBar.vue';

const route = useRoute();
const userStore = useUserStore();

const leaveDetail = ref<Leave>();

onMounted(() => {
    apiLeaveGet(Number(route.query.id), (data: ResultData) => {
        leaveDetail.value = data.data;
    });
});
</script>

<template>
    <div class="view">
        <right-slide-router-view></right-slide-router-view>
        <back-nav-bar class="view-header"></back-nav-bar>
        <div class="view-container">
            <div class="info-wrapper">
                <div class="header">
                    <van-image class="avatar" :src="userStore.userInfo.avatar" round width="50" height="50"></van-image>
                    <div class="title">{{ userStore.userInfo.name }}的请假申请</div>
                    <van-tag class="tag" plain :color="useStateColor(leaveDetail?.state!)">{{ i18n(leaveDetail?.state!, 'field.leave.state') }}</van-tag>
                </div>
                <div class="info">
                    <div class="cell">
                        <van-icon class="icon"></van-icon>
                        <div class="title">审批编号</div>
                        <div class="text">{{ leaveDetail?.id }}</div>
                    </div>
                    <div class="cell">
                        <van-icon class="icon"></van-icon>
                        <div class="title">提交时间</div>
                        <div class="text">{{ leaveDetail?.applyDatetime }}</div>
                    </div>
                    <div class="cell">
                        <van-icon class="icon"></van-icon>
                        <div class="title">所属班级</div>
                        <div class="text">{{ `${userStore.userInfo.department}/${userStore.userInfo.faculty}/${userStore.userInfo.major}/${userStore.userInfo._class}` }}</div>
                    </div>
                    <div class="cell">
                        <van-icon class="icon"></van-icon>
                        <div class="title">请假类型</div>
                        <div class="text">{{ i18n(leaveDetail?.category!, 'field.leave.category') }}</div>
                    </div>
                    <div class="cell">
                        <van-icon class="icon"></van-icon>
                        <div class="title">开始时间</div>
                        <div class="text">{{ leaveDetail?.startDatetime }}</div>
                    </div>
                    <div class="cell">
                        <van-icon class="icon"></van-icon>
                        <div class="title">结束时间</div>
                        <div class="text">{{ leaveDetail?.endDatetime }}</div>
                    </div>
                    <div class="cell">
                        <van-icon class="icon"></van-icon>
                        <div class="title">请假时长</div>
                        <div class="text">{{ useLeaveDuration(leaveDetail?.startDatetime!, leaveDetail?.endDatetime!) }}天</div>
                    </div>
                    <div class="cell">
                        <van-icon class="icon"></van-icon>
                        <div class="title">是否离校</div>
                        <div class="text"></div>
                    </div>
                    <div class="cell">
                        <van-icon class="icon"></van-icon>
                        <div class="title">夜不归宿</div>
                        <div class="text"></div>
                    </div>
                    <div class="cell">
                        <van-icon class="icon"></van-icon>
                        <div class="title">图片</div>
                        <div class="text"></div>
                    </div>
                </div>
            </div>
            <div class="contact-wrapper">

            </div>
            <div class="flow-wrapper">

            </div>
            <div class="button-group">
                <van-button
                    class="button cancel"
                    type="default"
                    round
                    plain
                    hairline
                    :disabled="leaveDetail?.state !== LeaveState.PENDING"
                >撤销申请</van-button>
                <van-button
                    class="button revoke"
                    type="primary"
                    round
                    plain
                    hairline
                    :disabled="leaveDetail?.state !== LeaveState.CANCEL"
                >申请销假</van-button>
            </div>
        </div>
    </div>
</template>

<style scoped lang="less">
.view-container {
    padding: 15px;

    .info-wrapper, .contact-wrapper, .flow-wrapper {
        margin: 16px auto;
        padding: 16px 8px;
        border-radius: var(--border-radius);
        background: #fff;
    }
    .info-wrapper {
        margin-top: 0;

        .header {
            display: flex;
            align-items: center;
            align-content: flex-start;

            .title {
                margin: 0 5px;
                font-weight: bold;
            }
            .tag {
                font-size: .68rem;
            }
        }
        .info {
            .cell {
                display: flex;
                align-items: center;
                justify-content: flex-start;
                margin: 16px auto;

                .icon, .title {
                    flex: 0 0 auto;
                    color: #888a;
                }
                .text {
                    margin-left: 16px;
                    line-height: 1.2rem;
                }
            }
        }
    }
    .button-group {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0 16px;

        .button {
            flex: 1 0 auto;
            margin: 0 5px;
        }
        .button.cancel {
            --van-button-default-border-color: #888;

            background-color: #0001;
        }
        .button.revoke {
            background-color: #56A9FB33;
        }
    }
}
</style>
