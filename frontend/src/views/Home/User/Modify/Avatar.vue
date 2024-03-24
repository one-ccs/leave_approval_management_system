<script setup lang="ts">
import { showFailToast, showSuccessToast, type UploaderFileListItem } from 'vant';
import BackNavBar from '@/components/BackNavBar.vue';
import { reactive } from 'vue';
import { apiUploadAvatar, apiUserPost } from '@/utils/api';
import type { ResponseData, User } from '@/utils/interface';
import encryptMD5 from '@/utils/encryptMD5';
import { useRoute } from 'vue-router';


const route = useRoute();
const form = reactive({
    annex: <UploaderFileListItem[]>[],
});
let avatarUrl = '';

const pictureAfterRead = (file: any) => {
    file.status = 'uploading';
    file.message = '上传中...';

    apiUploadAvatar({
        file: file.file,
        filename: encryptMD5(file.file.name + file.file.lastModified + file.file.size),
    }, (data: ResponseData) => {
        file.status = 'done';
        file.message = '上传完成';
        avatarUrl = data.data;

        showSuccessToast(data.message);
    }, (data: ResponseData) => {
        file.status = 'failed';
        file.message = '上传失败';

        showFailToast(data.message);
    });
};
const pictureOversize = (file: any) => {
    showFailToast('文件大小不能超过 1024 KB');
};
const onSubmit = () => {
    if (!avatarUrl) return showFailToast('提交失败\n没有获取到头像链接');

    apiUserPost({ id: Number(route.query.id) || null, avatar: avatarUrl } as User);
};
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <van-form @submit="onSubmit()">
                <van-cell-group>
                    <van-field
                        name="annex"
                        label="上传图片"
                        label-align="top"
                        :required="false"
                    >
                        <template #input>
                            <van-uploader
                                v-model="form.annex"
                                multiple
                                preview-size="6rem"
                                :after-read="pictureAfterRead"
                                :max-count="1"
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
                    <van-button round block type="primary" native-type="submit">提交</van-button>
                </van-cell-group>
            </van-form>
        </div>
    </div>
</template>

<style scoped lang="less">
.view-container {
    padding: 15px;

    .van-cell-group {
        margin-bottom: 15px;
        border-radius: var(--border-radius);
        overflow: hidden;
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
