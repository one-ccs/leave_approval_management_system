import { api } from '.';
import type { Teacher, TimeRangePageQuery } from "../interface";


export function apiTeacherGet(id: number, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/teacher',
        method: 'GET',
        params: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

export function apiTeacherPut(teacher: Teacher, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/teacher',
        method: 'PUT',
        data: {
            ...teacher,
        },
        successCallback,
        failureCallback,
    });
}

export function apiTeacherPost(teacher: Teacher, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/teacher',
        method: 'POST',
        data: {
            ...teacher,
        },
        successCallback,
        failureCallback,
    });
}

export function apiTeacherDelete(id: number, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/teacher',
        method: 'DELETE',
        data: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

export function apiTeacherPageQuery(query: TimeRangePageQuery, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/teacher/pageQuery',
        params: {
            ...query,
        },
        successCallback,
        failureCallback,
    });
}
