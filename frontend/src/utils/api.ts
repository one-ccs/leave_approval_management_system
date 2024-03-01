import { showSuccessToast, showFailToast } from 'vant';
import { localLoad, localSave } from './storage';
import request from './request';
import encryptMD5 from './encryptMD5';

const TOKEN_NAME = 'token';

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
function apiLogin(formData: any, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    const userData = {
        username: formData.username,
        password: encryptMD5(formData.password),
    };
    return request('/api/user/login', {
        method: 'post',
        data: userData,
        contentType: 'form',
        success: (data: any) => {
            if (formData.remember) localSave(TOKEN_NAME, userData);
            success && success(data);
        }
        ,failure
    });
}

export {
    apiLogin,
}
