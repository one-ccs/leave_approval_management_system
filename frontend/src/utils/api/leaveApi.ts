import { defaultSuccessCallback, defaultFailureCallback } from '.';
import type { Leave, LeavePageQuery } from '../interface';
import request from '../request';


/**
 * 获取请假条详情
 * @param id 请假条 id
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLeaveGet(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/leave', {
        params: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

/**
 * 添加请假条
 * @param data 请假条数据
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLeavePut(leave: Leave, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/leave', {
        data: {
            ...leave,
        },
        method: 'PUT',
        successCallback,
        failureCallback,
    });
}

/**
 * 修改请假条
 * @param data 请假条数据
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLeavePost(leave: Leave, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/leave', {
        data: {
            ...leave,
        },
        method: 'POST',
        successCallback,
        failureCallback,
    });
}

/**
 * 删除请假条
 * @param id 请假条 id
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLeaveDelete(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/leave', {
        data: {
            id,
        },
        method: 'DELETE',
        successCallback,
        failureCallback,
    });
}

/**
 * 分页查询请假条信息 (简要信息)
 * @param query 查询参数 { pageIndex, pageSize, state, category }
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLeavePageBrief(query: LeavePageQuery, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/leave/pageBrief', {
        params: {
            ...query,
            category: query.category === -1 ? undefined : query.category,
        },
        successCallback,
        failureCallback,
    });
}

/**
 * 撤销申请
 * @param id 请假条 id
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLeaveCancel(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/leave/cancel', {
        data: {
            id,
        },
        method: 'POST',
        successCallback,
        failureCallback,
    });
}

/**
 * 申请销假
 * @param id 请假条 id
 * @param position 定位 { longitude: 经度, latitude: 纬度 }
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLeaveRevoke(id: number, coords: { longitude: number, latitude: number }, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/leave/revoke', {
        data: {
            id,
            coords,
        },
        method: 'POST',
        contentType: 'JSON',
        successCallback,
        failureCallback,
    });
}

/**
 * 同意请假申请
 * @param id 请假条 id
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLeaveAgreeLeave(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/leave/agreeLeave', {
        data: {
            id,
        },
        method: 'POST',
        successCallback,
        failureCallback,
    });
}

/**
 * 驳回请假申请
 * @param id 请假条 id
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLeaveReject(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/leave/reject', {
        data: {
            id,
        },
        method: 'POST',
        successCallback,
        failureCallback,
    });
}

/**
 * 同意销假申请
 * @param id 请假条 id
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLeaveAgreeRevoke(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/leave/agreeRevoke', {
        data: {
            id,
        },
        method: 'POST',
        successCallback,
        failureCallback,
    });
}
