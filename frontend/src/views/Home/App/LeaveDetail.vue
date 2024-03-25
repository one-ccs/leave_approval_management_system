<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { showConfirmDialog, showSuccessToast } from 'vant';
import { ELeaveState, type Leave, type ResponseData } from '@/utils/interface';
import { apiLeaveAgreeLeave, apiLeaveAgreeRevoke, apiLeaveCancel, apiLeaveGet, apiLeaveReject, apiLeaveRevoke } from '@/utils/api';
import { useStateColor } from '@/utils/use';
import { getCurrentPosition } from '@/utils/advanced';
import i18n from '@/utils/i18n';
import useUserStore from '@/stores/user';
import RightSlideRouterView from '@/components/RightSlideRouterView.vue';
import BackNavBar from '@/components/BackNavBar.vue';
import Avatar from '@/components/Avatar.vue';

const route = useRoute();
const userStore = useUserStore();

interface LeaveExtra extends Leave {
    grade: string;
    major: string;
    _class: string;
}
const leaveDetail = ref<LeaveExtra>();
const cancelFlag = ref(false);
const revokeFlag = ref(false);
const rejectFlag = ref(false);
const agreeFlag = ref(false);

const onCancelClick = () => {
    showConfirmDialog({
        title: '提示',
        message: '确定要撤销申请吗？',
    }).then(() => {
        apiLeaveCancel(leaveDetail.value?.id!, (data: ResponseData) => {
            cancelFlag.value = true;
            leaveDetail.value!.state = ELeaveState.WITHDRAWN;
            showSuccessToast(data.message);
        });
    }).catch(() => {});
};
const onRevokeClick = () => {
    showConfirmDialog({
        title: '提示',
        message: '确定要申请销假吗？',
    }).then(() => {
        getCurrentPosition((pos) => {
            apiLeaveRevoke(leaveDetail.value?.id!, {
                longitude: pos.coords.longitude,
                latitude: pos.coords.latitude,
            }, (data: ResponseData) => {
                revokeFlag.value = true;
                leaveDetail.value!.state = ELeaveState.CANCELING;
                showSuccessToast(data.message);
            });
        });
    }).catch(() => {});
};
const onRejectClick = () => {
    showConfirmDialog({
        title: '提示',
        message: '确定要驳回申请吗？',
    }).then(() => {
        apiLeaveReject(leaveDetail.value?.id!, (data: ResponseData) => {
            rejectFlag.value = true;
            leaveDetail.value!.state = ELeaveState.REJECTED;
            showSuccessToast(data.message);
        });
    }).catch(() => {});
};
const onAgreeClick = () => {
    const stateZh = leaveDetail.value?.state === ELeaveState.PENDING ? '请假' : '销假';
    showConfirmDialog({
        title: '提示',
        message: `确定要同意${stateZh}申请吗？`,
    }).then(() => {
        // 同意请假申请
        if (leaveDetail.value?.state === ELeaveState.PENDING) {
            agreeFlag.value= true;
            leaveDetail.value.duration < 3 ?
                leaveDetail.value.state = ELeaveState.CANCEL :
                leaveDetail.value.state = ELeaveState.APPROVING;
            apiLeaveAgreeLeave(leaveDetail.value.id);
        }
        // 同意销假申请
        if (leaveDetail.value?.state === ELeaveState.CANCELING) {
            agreeFlag.value = true;
            leaveDetail.value.state = ELeaveState.DONE;
            apiLeaveAgreeRevoke(leaveDetail.value.id);
        }
    }).catch(() => {});
};

onMounted(() => {
    apiLeaveGet(Number(route.query.id), (data: ResponseData) => {
        leaveDetail.value = data.data;
    });
});
</script>

<template>
    <div class="view">
        <right-slide-router-view />
        <back-nav-bar class="view-header"></back-nav-bar>
        <div class="view-container">
            <div class="info-wrapper">
                <div class="header">
                    <avatar :key="userStore.userInfo.avatar" :src="userStore.userInfo.avatar" size="50"></avatar>
                    <div class="title">{{ userStore.userInfo.name }}的请假申请</div>
                    <van-tag
                        class="tag"
                        plain
                        :color="useStateColor(leaveDetail?.state!)"
                    >
                        {{ i18n(leaveDetail?.state!, 'field.leave.state') }}
                    </van-tag>
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
                    <div class="cell" v-if="leaveDetail?.rejectDatetime">
                        <van-icon class="icon"></van-icon>
                        <div class="title">驳回时间</div>
                        <div class="text">{{ leaveDetail?.rejectDatetime }}</div>
                    </div>
                    <div class="cell" v-if="leaveDetail?.rejectReason">
                        <van-icon class="icon"></van-icon>
                        <div class="title">驳回原因</div>
                        <div class="text">{{ leaveDetail?.rejectReason }}</div>
                    </div>
                    <div class="cell">
                        <van-icon class="icon"></van-icon>
                        <div class="title">所属班级</div>
                        <div class="text">{{ `${leaveDetail?.grade}${leaveDetail?.major}${leaveDetail?._class}班` }}</div>
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
                        <div class="text">{{ leaveDetail?.duration }}天</div>
                    </div>
                    <div class="cell">
                        <van-icon class="icon"></van-icon>
                        <div class="title">请假原因</div>
                        <div class="text">{{ leaveDetail?.leaveReason }}</div>
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
                    v-permiss="0x100"
                    class="button cancel"
                    type="default"
                    round
                    plain
                    hairline
                    :disabled="leaveDetail?.state !== ELeaveState.PENDING || cancelFlag"
                    @click="onCancelClick()"
                >撤销申请</van-button>
                <van-button
                    v-permiss="0x100"
                    class="button revoke"
                    type="primary"
                    round
                    plain
                    hairline
                    :disabled="leaveDetail?.state !== ELeaveState.CANCEL || revokeFlag"
                    @click="onRevokeClick()"
                >申请销假</van-button>

                <van-button
                    v-permiss="0x200"
                    class="button reject"
                    type="danger"
                    round
                    plain
                    hairline
                    :disabled="leaveDetail?.state !== ELeaveState.PENDING || rejectFlag"
                    @click="onRejectClick()"
                >驳回申请</van-button>
                <van-button
                    v-permiss="0x200"
                    class="button agree"
                    type="success"
                    round
                    plain
                    hairline
                    :disabled="leaveDetail?.state !== ELeaveState.PENDING && leaveDetail?.state !== ELeaveState.CANCELING || agreeFlag"
                    @click="onAgreeClick()"
                >同意申请</van-button>
            </div>
        </div>
    </div>
</template>

<style scoped lang="less">
.view-container {
    padding: 15px;

    .info-wrapper, .contact-wrapper, .flow-wrapper {
        margin: 16px auto;
        padding: 24px 16px;
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
                margin: 0 5px 0 9px;
                font-weight: bold;
            }
            .tag {
                font-size: .68rem;
            }
        }
        .info {
            font-size: .9rem;

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
        position: sticky;
        bottom: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0 16px;

        .button {
            flex: 1 0 auto;
            margin: 0 5px;
        }
        .button.cancel {
            --van-button-default-border-color: #c2c2c2;

            background-color: #c2c2c222;
        }
        .button.revoke {
            background-color: #1989FA22;
        }
        .button.reject {
            background-color: #EE0A2422;
        }
        .button.agree {
            background-color: #07C16022;
        }
    }
}
</style>
