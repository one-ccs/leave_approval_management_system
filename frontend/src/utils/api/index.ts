import { showSuccessToast, showFailToast } from 'vant';
import type { ResponseData } from '../interface';
import request, { type RequestConfig } from '../request';
import pinia from '@/stores/pinia';
import useUserStore from '@/stores/user';


const userStore = useUserStore(pinia);

/**
 * 默认成功处理函数
 * @param data 响应数据
 */
export function defaultSuccessCallback(data: ResponseData) {
    showSuccessToast(data.message);
}

/**
 * 默认失败处理函数
 * @param data 响应数据
 * @param status 响应状态码
 * @param url 请求地址
 */
export function defaultFailureCallback(data: ResponseData, status: number, url: string) {
    if (data.code === 401) return;
    showFailToast(data.message);
}

let isRefreshingToken = false;
async function refreshToken() {
    isRefreshingToken = true;

    try {
        const data = await request({
            url: '/api/user/refreshToken',
            method: 'POST',
        });
        if (data.code === 401.8) {
            userStore.clear();
            showFailToast("登录已过期\n请重新登录");
            setTimeout(() => {
                location.href = '/login';
            }, 800);
            return;
        }
        userStore.data.accessToken = data.data;
        userStore.save();
        onRefreshedToken(data.data);
    }
    finally {
        isRefreshingToken = false;
    }
}

let suspendedRequestCallbackQueue: Function[] = [];
function onRefreshedToken(token: string) {
    suspendedRequestCallbackQueue.forEach(callback => callback(token));
    suspendedRequestCallbackQueue.length = 0;
}
/**
 * 二次封装 添加默认回调函数 添加刷新令牌逻辑
 * @param config 请求配置
 * @returns
 */
export async function api(config: RequestConfig) {
    // 若正在刷新 token 则放入队列等待刷新完毕
    if (isRefreshingToken) {
        return new Promise((resolve, reject) => {
            suspendedRequestCallbackQueue.push((token: string) => {
                // 更新令牌
                if (!config.headers) config.headers = {};
                config.headers.Authorization = `Bearer ${token}`;
                // 发起请求
                resolve(request(config));
            });
        });
    }
    try {
        const data = await request({
            ...config,
            successCallback: config.successCallback || defaultSuccessCallback,
            failureCallback: config.failureCallback || defaultFailureCallback,
        });
        // 未登录
        if (data.code === 401) {
            showFailToast(`${data.message}\n即将跳转登录页...`);
            // userStore.clear();
            setTimeout(() => {
                // 使用 location.href 跳转 而不是 router 防止某些情况下页面不改变的 bug
                location.href = '/login';
            }, 800);
            return data;
        }
        // 登录已过期 尝试刷新令牌
        if (data.code === 401.8) {
            refreshToken();
            // 将当前请求放入队列 等待重试
            return new Promise((resolve, reject) => {
                suspendedRequestCallbackQueue.push((token: string) => {
                    // 更新令牌
                    if (!config.headers) config.headers = {};
                    config.headers.Authorization = `Bearer ${token}`;
                    // 发起请求
                    resolve(request(config));
                });
            });
        }
        return data;
    }
    catch(e) {}
}

export * from './userApi';
export * from './adminApi';
export * from './teacherApi';
export * from './studentApi';
export * from './leaveApi';
export * from './noticeApi';
export * from './uploadApi';
