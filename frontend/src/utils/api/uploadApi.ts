import { defaultFailureCallback, defaultSuccessCallback } from ".";
import request from "../request";
import useUserStore from '@/stores/user';


const { accessToken } = useUserStore().data;


export function apiUploadAvatar(data: { file: File, filename: string }, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/upload/avatar', {
        method: 'POST',
        data,
        token: accessToken,
        successCallback,
        failureCallback,
    });
}
