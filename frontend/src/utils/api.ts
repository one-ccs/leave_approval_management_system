import { closeToast, showLoadingToast, showSuccessToast, showFailToast } from 'vant';
import { localLoad, localRemove, localSave, sessionRemove, sessionSave } from './storage';
import request from './request';
import encryptMD5 from './encryptMD5';


export interface ResultData {
    code: number;
    message: string;
    data: any;
};

/**
 * 默认成功处理函数
 * @param message 提示消息
 */
function defaultSuccess(data: any) {
    showSuccessToast(data.message);
}

/**
 * 默认失败处理函数
 * @param url 请求地址
 * @param code 状态码
 */
function defaultFailure(data: any, status: number, url: string) {
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
function apiLogin(user: any, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    showLoadingToast({
        message: '登录中...',
        forbidClick: true,
    });
    return request('/api/user/login', {
        method: 'post',
        data: {
            username: user.username,
            password: encryptMD5(user.password),
            remember: user.remember,
        },
        contentType: 'form',
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

function apiLogout(success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/user/logout', {
        method: 'post',
        success,
        failure,
    });
}

export {
    apiLogin,
    apiLogout,
}
