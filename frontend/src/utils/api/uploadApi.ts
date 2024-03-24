import { defaultFailureCallback, defaultSuccessCallback } from ".";
import request from "../request";


export function apiUploadAvatar(data: { file: File, filename: string }, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/upload/avatar', {
        method: 'POST',
        data,
        successCallback,
        failureCallback,
    });
}
