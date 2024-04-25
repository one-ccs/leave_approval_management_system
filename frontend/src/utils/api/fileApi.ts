import { api } from '.';


export function apiUploadAvatar(data: { file: File, filename: string }, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/api/file/upload/avatar',
        method: 'POST',
        data,
        successCallback,
        failureCallback,
    });
}
