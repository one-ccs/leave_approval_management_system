import { defaultFailureCallback, defaultSuccessCallback } from ".";
import type { Student } from "../interface";
import request from "../request";


export function apiStudentGet(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/student', {
        method: 'GET',
        params: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

export function apiStudentPut(student: Student, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/student', {
        method: 'PUT',
        data: {
            ...student,
        },
        successCallback,
        failureCallback,
    });
}

export function apiStudentPost(student: Student, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/student', {
        method: 'POST',
        data: {
            ...student,
        },
        successCallback,
        failureCallback,
    });
}

export function apiStudentDelete(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/student', {
        method: 'DELETE',
        data: {
            id,
        },
        successCallback,
        failureCallback,
    });
}
