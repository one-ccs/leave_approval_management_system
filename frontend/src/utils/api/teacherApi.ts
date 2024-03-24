import { defaultFailureCallback, defaultSuccessCallback } from ".";
import type { Teacher, TimeRangePageQuery } from "../interface";
import request from "../request";


export function apiTeacherGet(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/teacher', {
        method: 'GET',
        params: {
            id,
        },
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
        successCallback,
        failureCallback,
    });
}

export function apiTeacherPageQuery(query: TimeRangePageQuery, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/teacher/pageQuery', {
        params: {
            ...query,
        },
        successCallback,
        failureCallback,
    });
}
