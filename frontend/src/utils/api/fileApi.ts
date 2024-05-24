import { api } from '.';


export function apiUploadAvatar(data: { file: File, filename: string }, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/file/image/avatar',
        method: 'POST',
        data,
        successCallback,
        failureCallback,
    });
}

export function apiUploadLeave(data: { file: File, filename: string }, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/file/image/leave',
        method: 'POST',
        data,
        successCallback,
        failureCallback,
    });
}
