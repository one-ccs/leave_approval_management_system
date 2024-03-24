<script setup lang="ts">
import { computed, ref } from 'vue';
import { useRouter } from 'vue-router';
import { showFailToast, showSuccessToast, type UploaderFileListItem } from 'vant';
import type { Leave, ResponseData, LeaveAddForm } from '@/utils/interface';
import { apiLeavePut } from '@/utils/api';
import { useLeaveDuration } from '@/utils/use';
import BackNavBar from '@/components/BackNavBar.vue';
import { reactive } from 'vue';

const router = useRouter();
const categoryPickerShown = ref(false);
const startDatetimePickerShown = ref(false);
const endDatetimePickerShown = ref(false);
const leaveForm = reactive<LeaveAddForm>({
    category: 0,
    startDatetime: '',
    endDatetime: '',
    leaveSchool: false,
    leaveReason: '',
});
const leaveFormShadow = ref({
    category: '',
    startDatetime: {
        date: <string[]>[],
        time: <string[]>[],
    },
    endDatetime: {
        date: <string[]>[],
        time: <string[]>[],
    },
    duration: '0 天',
    annex: <UploaderFileListItem[]>[],
});
const durationValue = computed(() => {
    return parseInt(leaveFormShadow.value.duration);
})

const formRules = {
    category: [
        { required: true, message: '请选择请假类别' },
    ],
    startDatetime: [
        { required: true, message: '请选择开始时间' },
    ],
    endDatetime: [
        { required: true, message: '请选择结束时间' },
    ],
    leaveReason: [
        { required: true, message: '请输入请假原因' },
    ],
};
const category = [
    {
        text: '事假',
        value: 0,
    },
    {
        text: '病假',
        value: 1,
    },
    {
        text: '公假',
        value: 2,
    },
    {
        text: '出校申请',
        value: 3,
    },
];

const confirmCategory = ({ selectedOptions }: any) => {
    categoryPickerShown.value = false;
    leaveForm.category = selectedOptions[0].value;
    leaveFormShadow.value.category = selectedOptions[0].text;
};
const openStartDatetimePicker = () => {
    startDatetimePickerShown.value = true;
    const datetime = new Date();
    leaveFormShadow.value.startDatetime.date = [
        String(datetime.getFullYear()),
        ('00' + (datetime.getMonth() + 1)).slice(String(datetime.getMonth() + 1).length),
        ('00' + (datetime.getDate())).slice(String(datetime.getDate()).length),
    ];
    leaveFormShadow.value.startDatetime.time = [
        ('00' + (datetime.getHours())).slice(String(datetime.getHours()).length),
        ('00' + (datetime.getMinutes())).slice(String(datetime.getMinutes()).length),
    ];
};
const confirmStartDatetime = () => {
    startDatetimePickerShown.value = false;
    const [yyyy, mm, dd, HH, MM] = [
        ...leaveFormShadow.value.startDatetime.date,
        ...leaveFormShadow.value.startDatetime.time,
    ];
    leaveForm.startDatetime = `${yyyy}-${mm}-${dd} ${HH}:${MM}`;
    if (leaveForm.endDatetime) {
        const duration = useLeaveDuration(
            leaveForm.startDatetime,
            leaveForm.endDatetime
        );
        if (duration > 0) leaveFormShadow.value.duration = duration + ' 天';
        else {
            leaveForm.startDatetime = '';
            showFailToast('时间选择有误');
        }
    }
};
const openEndDatetimePicker = () => {
    endDatetimePickerShown.value = true;
    const datetime = new Date();
    leaveFormShadow.value.endDatetime.date = [
        String(datetime.getFullYear()),
        ('00' + (datetime.getMonth() + 1)).slice(String(datetime.getMonth() + 1).length),
        ('00' + (datetime.getDate())).slice(String(datetime.getDate()).length),
    ];
    leaveFormShadow.value.endDatetime.time = [
        ('00' + (datetime.getHours())).slice(String(datetime.getHours()).length),
        ('00' + (datetime.getMinutes())).slice(String(datetime.getMinutes()).length),
    ];
};
const confirmEndDatetime = () => {
    endDatetimePickerShown.value = false;
    const [yyyy, mm, dd, HH, MM] = [
        ...leaveFormShadow.value.endDatetime.date,
        ...leaveFormShadow.value.endDatetime.time,
    ];
    leaveForm.endDatetime = `${yyyy}-${mm}-${dd} ${HH}:${MM}`;
    if (leaveForm.startDatetime) {
        const duration = useLeaveDuration(
            leaveForm.startDatetime,
            leaveForm.endDatetime
        );
        if (duration > 0) leaveFormShadow.value.duration = duration + ' 天';
        else {
            leaveForm.endDatetime = '';
            showFailToast('时间选择有误');
        }
    }
};
const pictureAfterRead = (file: any) => {
    file.status = 'uploading';
    file.message = '上传中...'

    console.log(file);

    setTimeout(() => {
        file.status = 'done';
        file.message = '上传完成'
    }, 1000);
};
const pictureOversize = (file: any) => {
    showFailToast('文件大小不能超过 1024 KB')
};
const onSubmit = () => {
    apiLeavePut(leaveForm as unknown as Leave, (data: ResponseData) => {
        showSuccessToast(data.message);
        router.back();
    });
};
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <van-form @submit="onSubmit()" required>
                <van-cell-group inset>
                    <van-field
                        v-model="leaveFormShadow.category"
                        name="category"
                        input-align="right"
                        icon-prefix="fa"
                        right-icon="caret-down"
                        clickable
                        readonly
                        label="请假类别"
                        placeholder="选择请假类别"
                        @click="categoryPickerShown = true"
                        :rules="formRules.category"
                        error-message-align="right"
                    />
                    <van-popup v-model:show="categoryPickerShown" round position="bottom">
                        <van-picker
                            :columns="category"
                            @cancel="categoryPickerShown = false"
                            @confirm="confirmCategory"
                        />
                    </van-popup>
                </van-cell-group>

                <van-cell-group inset>
                    <van-field
                        v-model="leaveForm.startDatetime"
                        name="startDatetime"
                        input-align="right"
                        icon-prefix="fa"
                        right-icon="caret-down"
                        clickable
                        readonly
                        label="开始时间"
                        placeholder="选择开始时间"
                        @click="openStartDatetimePicker"
                        :rules="formRules.startDatetime"
                        error-message-align="right"
                    />
                    <van-popup v-model:show="startDatetimePickerShown" round position="bottom">
                        <van-picker-group
                            :tabs="['选择日期', '选择时间']"
                            @cancel="startDatetimePickerShown = false"
                            @confirm="confirmStartDatetime"
                        >
                            <van-date-picker v-model="leaveFormShadow.startDatetime.date"/>
                            <van-time-picker v-model="leaveFormShadow.startDatetime.time"/>
                        </van-picker-group>
                    </van-popup>

                    <van-field
                        v-model="leaveForm.endDatetime"
                        name="endDatetime"
                        input-align="right"
                        icon-prefix="fa"
                        right-icon="caret-down"
                        clickable
                        readonly
                        label="结束时间"
                        placeholder="选择结束时间"
                        @click="openEndDatetimePicker"
                        :rules="formRules.endDatetime"
                        error-message-align="right"
                    />
                    <van-popup v-model:show="endDatetimePickerShown" round position="bottom">
                        <van-picker-group
                            :tabs="['选择日期', '选择时间']"
                            @cancel="endDatetimePickerShown = false"
                            @confirm="confirmEndDatetime"
                        >
                            <van-date-picker v-model="leaveFormShadow.endDatetime.date"/>
                            <van-time-picker v-model="leaveFormShadow.endDatetime.time"/>
                        </van-picker-group>
                    </van-popup>

                    <van-field
                        v-model="leaveFormShadow.duration"
                        input-align="right"
                        readonly
                        label="请假时长"
                    ></van-field>
                </van-cell-group>

                <van-cell-group inset>
                    <van-field
                        label="是否离校"
                        input-align="right"
                    >
                        <template #input>
                            <van-switch v-model="leaveForm.leaveSchool" size="1.25rem" />
                        </template>
                    </van-field>
                </van-cell-group>

                <van-cell-group inset>
                    <van-field
                        v-model="leaveForm.leaveReason"
                        rows="3"
                        autosize
                        label-align="top"
                        label="请假原因"
                        type="textarea"
                        maxlength="200"
                        placeholder="请输入请假原因（200字以内）"
                        show-word-limit
                        :rules="formRules.leaveReason"
                        error-message-align="right"
                    />
                </van-cell-group>

                <van-cell-group inset>
                    <van-field
                        name="annex"
                        label="上传图片"
                        label-align="top"
                        :required="false"
                    >
                        <template #input>
                            <van-uploader
                                v-model="leaveFormShadow.annex"
                                multiple
                                preview-size="6rem"
                                :after-read="pictureAfterRead"
                                :max-count="3"
                                :max-size="1024 * 1024"
                                @oversize="pictureOversize"
                                :preview-options="{
                                    closeable: true,
                                    closeIcon: 'close',
                                }"
                                result-type="dataUrl"
                                upload-text="添加图片"
                            >
                                <template #preview-cover="{ file }">
                                    <div class="preview-cover van-ellipsis">{{ file.name }}</div>
                                </template>
                            </van-uploader>
                        </template>
                    </van-field>
                </van-cell-group>

                <van-cell-group inset>
                    <van-cell title="审批流程"></van-cell>
                    <van-cell
                        v-if="durationValue > 0"
                        title="审批人·未开始"
                        icon-prefix="fa"
                        icon="user-o"
                        label="辅导员"
                        value="未开始"
                    ></van-cell>
                    <van-cell
                        v-if="durationValue >= 3"
                        title="审批人·未开始"
                        icon="manager-o"
                        label="学院老师"
                        value="未开始"
                    ></van-cell>
                </van-cell-group>

                <van-cell-group inset>
                    <van-button round block type="primary" native-type="submit">提交</van-button>
                </van-cell-group>
            </van-form>
        </div>
    </div>
</template>

<style scoped lang="less">
.view-container {
    .van-cell-group {
        margin-top: 15px;
    }
    .preview-cover {
        position: absolute;
        bottom: 0;
        padding: 0 5px;
        width: 100%;
        color: #fff;
        font-size: .8rem;
        text-align: center;
        background: #0005;
    }
}
</style>
