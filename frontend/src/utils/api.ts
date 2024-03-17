import { closeToast, showLoadingToast, showSuccessToast, showFailToast } from 'vant';
import type { ResultData, LeavePageQuery, Leave } from './interface';
import request from './request';
import encryptMD5 from './encryptMD5';


/**
 * 默认成功处理函数
 * @param message 提示消息
 */
function defaultSuccess(data: ResultData) {
    showSuccessToast(data.message);
}

/**
 * 默认失败处理函数
 * @param url 请求地址
 * @param code 状态码
 */
function defaultFailure(data: ResultData, status: number, url: string) {
    if (data.code === 401) return;
    showFailToast(data.message);
}

/**
 * 登录
 * @param username 用户名
 * @param password 密码
 * @param remember 是否记住
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLogin(user: any, successCallback: Function = defaultSuccess, failureCallback: Function = defaultFailure) {
    showLoadingToast({
        message: '登录中...',
        forbidClick: true,
    });
    return request('/api/user/login', {
        method: 'POST',
        data: {
            username: user.username,
            password: encryptMD5(user.password),
            remember: user.remember,
        },
        successCallback: (data: ResultData) => {
            closeToast();
            successCallback && successCallback(data);
        },
        failureCallback: (data: ResultData) => {
            closeToast();
            failureCallback && failureCallback(data);
        }
    });
}

/**
 * 登出
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLogout(successCallback: Function = defaultSuccess, failureCallback: Function = defaultFailure) {
    return request('/api/user/logout', {
        method: 'POST',
        successCallback,
        failureCallback,
    });
}

/**
 * 获取请假条详情
 * @param id 请假条 id
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLeaveGet(id: number, successCallback: Function = defaultSuccess, failureCallback: Function = defaultFailure) {
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
export function apiLeavePut(data: Leave, successCallback: Function = defaultSuccess, failureCallback: Function = defaultFailure) {
    return request('/api/leave', {
        data,
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
export function apiLeavePost(data: Leave, successCallback: Function = defaultSuccess, failureCallback: Function = defaultFailure) {
    return request('/api/leave', {
        data,
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
export function apiLeaveDelete(id: number, successCallback: Function = defaultSuccess, failureCallback: Function = defaultFailure) {
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
export function apiLeavePageBrief(query: LeavePageQuery, successCallback: Function = defaultSuccess, failureCallback: Function = defaultFailure) {
    return request('/api/leave/brief', {
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
export function apiLeaveCancel(id: number, successCallback: Function = defaultSuccess, failureCallback: Function = defaultFailure) {
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
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLeaveRevoke(id: number, successCallback: Function = defaultSuccess, failureCallback: Function = defaultFailure) {
    return request('/api/leave/revoke', {
        data: {
            id,
        },
        method: 'POST',
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
export function apiLeaveAgreeLeave(id: number, successCallback: Function = defaultSuccess, failureCallback: Function = defaultFailure) {
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
export function apiLeaveReject(id: number, successCallback: Function = defaultSuccess, failureCallback: Function = defaultFailure) {
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
export function apiLeaveAgreeRevoke(id: number, successCallback: Function = defaultSuccess, failureCallback: Function = defaultFailure) {
    return request('/api/leave/agreeRevoke', {
        data: {
            id,
        },
        method: 'POST',
        successCallback,
        failureCallback,
    });
}
