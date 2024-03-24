import { defaultFailureCallback, defaultSuccessCallback } from ".";
import type { Admin, TimeRangePageQuery } from "../interface";
import request from "../request";


export function apiAdminGet(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/admin', {
        method: 'GET',
        params: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

export function apiAdminPut(admin: Admin, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/admin', {
        method: 'PUT',
        data: {
            ...admin,
        },
        successCallback,
        failureCallback,
    });
}

export function apiAdminPost(admin: Admin, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/admin', {
        method: 'POST',
        data: {
            ...admin,
        },
        successCallback,
        failureCallback,
    });
}

export function apiAdminDelete(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/admin', {
        method: 'DELETE',
        data: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

export function apiAdminPageQuery(query: TimeRangePageQuery, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/admin/pageQuery', {
        params: {
            ...query,
        },
        successCallback,
        failureCallback,
    });
}
