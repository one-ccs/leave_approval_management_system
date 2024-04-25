import { api } from '.';
import type { Student, TimeRangePageQuery } from "../interface";


export function apiStudentGet(id: number, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/api/student',
        method: 'GET',
        params: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

export function apiStudentPut(student: Student, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/api/student',
        method: 'PUT',
        data: {
            ...student,
        },
        successCallback,
        failureCallback,
    });
}

export function apiStudentPost(student: Student, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/api/student',
        method: 'POST',
        data: {
            ...student,
        },
        successCallback,
        failureCallback,
    });
}

export function apiStudentDelete(id: number, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/api/student',
        method: 'DELETE',
        data: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

export function apiStudentPageQuery(query: TimeRangePageQuery, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/api/student/pageQuery',
        params: {
            ...query,
        },
        successCallback,
        failureCallback,
    });
}
