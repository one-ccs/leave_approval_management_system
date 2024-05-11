import { api } from '.';
import type { Notice, TimeRangePageQuery } from "../interface";


export function apiNoticeGet(id: number, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/notice',
        method: 'GET',
        params: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

export function apiNoticePut(notice: Notice, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/notice',
        method: 'PUT',
        data: {
            ...notice,
        },
        successCallback,
        failureCallback,
    });
}

export function apiNoticePost(notice: Notice, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/notice',
        method: 'POST',
        data: {
            ...notice,
        },
        successCallback,
        failureCallback,
    });
}

export function apiNoticeDelete(id: number, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/notice',
        method: 'DELETE',
        data: {
            id,
        },
        successCallback,
        failureCallback,
    });
}
export function apiNoticeDetail(id: number, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/notice/detail',
        params: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

export function apiNoticePageQuery(query: TimeRangePageQuery, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/notice/pageQuery',
        params: {
            ...query,
        },
        successCallback,
        failureCallback,
    });
}
