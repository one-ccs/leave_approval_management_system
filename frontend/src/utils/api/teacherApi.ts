import { defaultFailureCallback, defaultSuccessCallback } from ".";
import type { Teacher, TimeRangePageQuery } from "../interface";
import request from "../request";
import useUserStore from '@/stores/user';


const { accessToken } = useUserStore().data;


export function apiTeacherGet(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/teacher', {
        method: 'GET',
        params: {
            id,
        },
        token: accessToken,
        successCallback,
        failureCallback,
    });
}

export function apiTeacherPut(teacher: Teacher, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/teacher', {
        method: 'PUT',
        data: {
            ...teacher,
        },
        token: accessToken,
        successCallback,
        failureCallback,
    });
}

export function apiTeacherPost(teacher: Teacher, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/teacher', {
        method: 'POST',
        data: {
            ...teacher,
        },
        token: accessToken,
        successCallback,
        failureCallback,
    });
}

export function apiTeacherDelete(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/teacher', {
        method: 'DELETE',
        data: {
            id,
        },
        token: accessToken,
        successCallback,
        failureCallback,
    });
}

export function apiTeacherPageQuery(query: TimeRangePageQuery, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/teacher/pageQuery', {
        params: {
            ...query,
        },
        token: accessToken,
        successCallback,
        failureCallback,
    });
}
