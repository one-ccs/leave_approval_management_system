import { api } from '.';
import type { Assistant, TimeRangePageQuery } from "../interface";


export function apiAssistantGet(id: number, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/assistant',
        method: 'GET',
        params: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

export function apiAssistantPut(assistant: Assistant, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/assistant',
        method: 'PUT',
        data: {
            ...assistant,
        },
        successCallback,
        failureCallback,
    });
}

export function apiAssistantPost(assistant: Assistant, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/assistant',
        method: 'POST',
        data: {
            ...assistant,
        },
        successCallback,
        failureCallback,
    });
}

export function apiAssistantDelete(id: number, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/assistant',
        method: 'DELETE',
        data: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

export function apiAssistantPageQuery(query: TimeRangePageQuery, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/assistant/pageQuery',
        params: {
            ...query,
        },
        successCallback,
        failureCallback,
    });
}
