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

/**
 * 登出
 * @param success 成功回调函数
 * @param failure 失败回调函数
 * @returns Promise
 */
export function apiLogout(success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/user/logout', {
        method: 'POST',
        success,
        failure,
    });
}

/**
 * 获取请假条详情
 * @param id 请假条 id
 * @param success 成功回调函数
 * @param failure 失败回调函数
 * @returns Promise
 */
export function apiLeaveGet(id: number, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/leave', {
        params: {
            id,
        },
        success,
        failure,
    });
}

/**
 * 添加请假条
 * @param data 请假条数据
 * @param success 成功回调函数
 * @param failure 失败回调函数
 * @returns Promise
 */
export function apiLeavePut(data: Leave, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/leave', {
        data,
        method: 'PUT',
        success,
        failure,
    });
}

/**
 * 修改请假条
 * @param data 请假条数据
 * @param success 成功回调函数
 * @param failure 失败回调函数
 * @returns Promise
 */
export function apiLeavePost(data: Leave, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/leave', {
        data,
        method: 'POST',
        success,
        failure,
    });
}
/**
 * 删除请假条
 * @param id 请假条 id
 * @param success 成功回调函数
 * @param failure 失败回调函数
 * @returns Promise
 */
export function apiLeaveDelete(id: number, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/leave', {
        data: {
            id,
        },
        method: 'DELETE',
        success,
        failure,
    });
}

/**
 * 分页查询请假条信息 (简要信息)
 * @param query 查询参数 { pageIndex, pageSize, state, category }
 * @param success 成功回调函数
 * @param failure 失败回调函数
 * @returns Promise
 */
export function apiLeavePageBrief(query: LeavePageQuery, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/leave/brief', {
        params: {
            ...query,
            category: query.category === -1 ? undefined : query.category,
        },
        success,
        failure,
    });
}

/**
 * 撤销申请
 * @param id 请假条 id
 * @param success 成功回调函数
 * @param failure 失败回调函数
 * @returns Promise
 */
export function apiLeaveCancel(id: number, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/leave/cancel', {
        data: {
            id,
        },
        method: 'POST',
        success,
        failure,
    });
}

/**
 * 申请销假
 * @param id 请假条 id
 * @param success 成功回调函数
 * @param failure 失败回调函数
 * @returns Promise
 */
export function apiLeaveRevoke(id: number, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/leave/revoke', {
        data: {
            id,
        },
        method: 'POST',
        success,
        failure,
    });
}

/**
 * 同意请假申请
 * @param id 请假条 id
 * @param success 成功回调函数
 * @param failure 失败回调函数
 * @returns Promise
 */
export function apiLeaveAgreeLeave(id: number, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/leave/agree', {
        data: {
            id,
        },
        method: 'POST',
        success,
        failure,
    });
}

/**
 * 驳回请假申请
 * @param id 请假条 id
 * @param success 成功回调函数
 * @param failure 失败回调函数
 * @returns Promise
 */
export function apiLeaveReject(id: number, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/leave/reject', {
        data: {
            id,
        },
        method: 'POST',
        success,
        failure,
    });
}

/**
 * 同意销假申请
 * @param id 请假条 id
 * @param success 成功回调函数
 * @param failure 失败回调函数
 * @returns Promise
 */
export function apiLeaveAgreeRevoke(id: number, success: Function = defaultSuccess, failure: Function = defaultFailure) {
    return request('/api/leave/agreeRevoke', {
        data: {
            id,
        },
        method: 'POST',
        success,
        failure,
    });
}
