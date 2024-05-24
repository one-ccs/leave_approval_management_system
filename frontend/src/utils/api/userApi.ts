import { api } from '.';
import type { User, LoginUser, TimeRangePageQuery } from '../interface';
import encryptMD5 from '../encryptMD5';


/**
 * 获取用户信息
 * @param id 用户 id
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiUserGet(id: number, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/user',
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
export function apiUserPut(user: User, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/user',
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
export function apiUserPost(user: User, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/user',
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
export function apiUserDelete(id: number, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/user',
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
export function apiUserPageQuery(query: TimeRangePageQuery, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/user',
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
export function apiLogin(user: LoginUser, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/user/login',
        method: 'POST',
        data: {
            ...user,
            password: encryptMD5(user.password),
        },
        successCallback,
        failureCallback,
    });
}

/**
 * 刷新令牌 api
 * @returns Promise
 */
export function apiRefreshToken() {
    return api({
        url: '/user/refreshToken',
        method: 'POST',
    });
}

/**
 * 登出
 * @param successCallback 成功回调函数
 * @param failureCallback 失败回调函数
 * @returns Promise
 */
export function apiLogout(successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/user/logout',
        method: 'POST',
        successCallback,
        failureCallback,
    });
}

/**
 * 修改手机号码
 * @param data 手机号与验证码
 * @param successCallback
 * @param failureCallback
 */
export function apiModifyTelephone(data: { telephone: string, captcha: string }, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/user/modifyTelephone',
        method: 'POST',
        data: {
            ...data,
        },
        successCallback,
        failureCallback,
    });
}

/**
 * 修改密码
 * @param data 密码与验证码
 * @param successCallback
 * @param failureCallback
 */
export function apiModifyPassword(data: { password: string, captcha: string }, successCallback?: Function, failureCallback?: Function) {
    return api({
		url: '/user/modifyPassword',
        method: 'POST',
        data: {
            ...data,
            password: encryptMD5(data.password),
        },
        successCallback,
        failureCallback,
    });
}
