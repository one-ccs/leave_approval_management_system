import { api } from '.';
import type { Admin, TimeRangePageQuery } from "../interface";


export function apiAdminGet(id: number, successCallback?: Function, failureCallback?: Function) {
    return api({
        url: '/api/admin',
        method: 'GET',
        params: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

export function apiAdminPut(admin: Admin, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/api/admin',
        method: 'PUT',
        data: {
            ...admin,
        },
        successCallback,
        failureCallback,
    });
}

export function apiAdminPost(admin: Admin, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/api/admin',
        method: 'POST',
        data: {
            ...admin,
        },
        successCallback,
        failureCallback,
    });
}

export function apiAdminDelete(id: number, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/api/admin',
        method: 'DELETE',
        data: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

export function apiAdminPageQuery(query: TimeRangePageQuery, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/api/admin/pageQuery',
        params: {
            ...query,
        },
        successCallback,
        failureCallback,
    });
}
