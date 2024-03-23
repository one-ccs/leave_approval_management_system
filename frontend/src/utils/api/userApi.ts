import { closeToast, showLoadingToast } from 'vant';
import { defaultSuccessCallback, defaultFailureCallback } from '.';
import type { ResponseData, User, LoginUser, TimeRangePageQuery } from '../interface';
import request from '../request';
import encryptMD5 from '../encryptMD5';


/**
 * 获取用户信息
 * @param id 用户 id
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiUserGet(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/user', {
        params: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

/**
 * 添加用户信息
 * @param user 用户信息
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiUserPut(user: User, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/user', {
        method: 'PUT',
        data: {
            ...user,
        },
        successCallback,
        failureCallback,
    });
}

/**
 * 修改用户信息
 * @param user 用户信息
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiUserPost(user: User, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/user', {
        method: 'POST',
        data: {
            ...user,
        },
        successCallback,
        failureCallback,
    });
}

/**
 * 删除用户信息
 * @param id 用户 id
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiUserDelete(id: number, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/user', {
        method: 'PUT',
        data: {
            id,
        },
        successCallback,
        failureCallback,
    });
}

/**
 * 分页查询用户信息
 * @param query 查询参数 { pageIndex, pageSize, query, startDatetime, endDatetime }
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiUserPageQuery(query: TimeRangePageQuery, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/user', {
        data: {
            ...query,
        },
        successCallback,
        failureCallback,
    });
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
export function apiLogin(user: LoginUser, successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
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
        successCallback: (data: ResponseData) => {
            closeToast();
            successCallback && successCallback(data);
        },
        failureCallback: (data: ResponseData) => {
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
export function apiLogout(successCallback: Function = defaultSuccessCallback, failureCallback: Function = defaultFailureCallback) {
    return request('/api/user/logout', {
        method: 'POST',
        successCallback,
        failureCallback,
    });
}
