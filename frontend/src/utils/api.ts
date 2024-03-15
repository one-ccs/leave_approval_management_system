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
 * @param success 成功回调函数
 * @param failure 失败回调函数
 * @returns Promise
 */
export function apiLogin(user: any, success: Function = defaultSuccess, failure: Function = defaultFailure) {
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
        success: (data: ResultData) => {
            closeToast();
            success && success(data);
        },
        failure: (data: ResultData) => {
            closeToast();
            failure && failure(data);
        }
    });
}

export function apiLogout(success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/user/logout', {
        method: 'POST',
        success,
        failure,
    });
}

export function apiLeaveGet(query: LeavePageQuery, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/leave', {
        params: {
            ...query,
            category: query.category === -1 ? undefined : query.category,
        },
        success,
        failure,
    });
}

export function apiLeavePut(query: Leave, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/leave', {
        data: query,
        method: 'PUT',
        success,
        failure,
    });
}

export function apiLeavePost(query: Leave, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/leave', {
        data: query,
        method: 'POST',
        success,
        failure,
    });
}

export function apiLeaveDelete(query: LeavePageQuery, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/leave', {
        data: query,
        method: 'DELETE',
        success,
        failure,
    });
}
