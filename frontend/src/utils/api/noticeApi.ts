import { defaultFailureCallback, defaultSuccessCallback } from ".";
import type { Notice, TimeRangePageQuery } from "../interface";
import request from "../request";
import useUserStore from '@/stores/user';


const { accessToken } = useUserStore().data;


export function apiNoticeGet(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/notice', {
        method: 'GET',
        params: {
            id,
        },
        token: accessToken,
        successCallback,
        failureCallback,
    });
}

export function apiNoticePut(notice: Notice, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/notice', {
        method: 'PUT',
        data: {
            ...notice,
        },
        token: accessToken,
        successCallback,
        failureCallback,
    });
}

export function apiNoticePost(notice: Notice, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/notice', {
        method: 'POST',
        data: {
            ...notice,
        },
        token: accessToken,
        successCallback,
        failureCallback,
    });
}

export function apiNoticeDelete(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/notice', {
        method: 'DELETE',
        data: {
            id,
        },
        token: accessToken,
        successCallback,
        failureCallback,
    });
}

export function apiNoticePageQuery(query: TimeRangePageQuery, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/notice/pageQuery', {
        params: {
            ...query,
        },
        token: accessToken,
        successCallback,
        failureCallback,
    });
}
