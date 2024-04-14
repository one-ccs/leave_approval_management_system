import { defaultFailureCallback, defaultSuccessCallback } from ".";
import type { Admin, TimeRangePageQuery } from "../interface";
import request from "../request";
import useUserStore from '@/stores/user';


const userStore = useUserStore();


export function apiAdminGet(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/admin', {
        method: 'GET',
        params: {
            id,
        },
        token: userStore.data.accessToken,
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
        token: userStore.data.accessToken,
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
        token: userStore.data.accessToken,
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
        token: userStore.data.accessToken,
        successCallback,
        failureCallback,
    });
}

export function apiAdminPageQuery(query: TimeRangePageQuery, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/admin/pageQuery', {
        params: {
            ...query,
        },
        token: userStore.data.accessToken,
        successCallback,
        failureCallback,
    });
}
