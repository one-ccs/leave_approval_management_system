
import axios, { type AxiosInstance, type AxiosError, type AxiosResponse, type InternalAxiosRequestConfig } from 'axios';
import { showFailToast } from 'vant';
import { apiRefreshToken } from './api/userApi';
import pinia from '@/stores/pinia';
import useGlobalStore from '@/stores/global';
import useUserStore from '@/stores/user';


const globalStore = useGlobalStore(pinia);
const userStore = useUserStore(pinia);


const service: AxiosInstance = axios.create({
    baseURL: globalStore.apiHost,
    timeout: globalStore.timeout,
    // 小于 500 的状态码不抛出错误
    validateStatus: status => (status < 500),
});

// 令牌刷新逻辑
const refreshTokenApi = '/user/refreshToken';
let isRefreshingToken = false;
let repeatRequestQueue: Function[] = [];
let repeatResponseQueue: Function[] = [];
/**
 * 将请求添加到重播队列等待重播
 * @param config 请求配置
 * @param source 请求来源 request 响应拦截器 response 请求拦截器
 * @returns Promise
 */
function repeatRequest(config: InternalAxiosRequestConfig, source: 'request' | 'response'): Promise<InternalAxiosRequestConfig> {

    console.log('重播', config.url, source);
    if (source === 'request') {
        // 在请求拦截中添加的重播
        return new Promise((resolve, reject) => {
            repeatRequestQueue.push((token: string) => {
                config.headers.Authorization = `Bearer ${token}`;
                resolve(config);
            });
        });
    }
    // 在响应拦截中添加的重播
    return new Promise((resolve, reject) => {
        repeatResponseQueue.push((token: string) => {
            config.headers.Authorization = `Bearer ${token}`;
            resolve(axios(config));
        });
    });
}
/**
 * token 刷新事件（重播请求）
 * @param token 新 token
 */
function onRefreshedToken(token: string) {
    repeatRequestQueue.forEach(func => func(token));
    repeatRequestQueue.length = 0;

    repeatResponseQueue.forEach(func => func(token));
    repeatResponseQueue.length = 0;
}

// 请求拦截器
service.interceptors.request.use(
    (config: InternalAxiosRequestConfig) => {
        // 若正在刷新 token 则放入队列等待刷新完毕
        if (isRefreshingToken && config.url !== refreshTokenApi) {
            return repeatRequest(config, 'request');
        }
        // 设置 token
        config.headers.Authorization = config.url === refreshTokenApi ?
            `Bearer ${userStore.data.refreshToken}` :
            `Bearer ${userStore.data.accessToken}`;
        return config;
    },
    (error: AxiosError) => {
        return Promise.reject(error);
    }
);

// 响应拦截器
service.interceptors.response.use(
    async (response: AxiosResponse) => {
        // 未登录
        if (response.data.code === 401) {
            showFailToast(`${response.data.message}\n即将跳转登录页...`);
            userStore.clear();
            setTimeout(() => {
                // 使用 location.href 跳转 而不是 router 防止某些情况下页面不改变的 bug
                location.href = '/login';
            }, 800);
            return response;
        }
        // 登录已过期 尝试刷新令牌
        if (response.data.code === 401.8 && !isRefreshingToken) {
            // 刷新令牌
            isRefreshingToken = true;

            try {
                const data = await apiRefreshToken();

                if (data.code === 401.8) {
                    showFailToast("登录已过期\n请重新登录");
                    userStore.clear();
                    setTimeout(() => {
                        location.href = '/login';
                    }, 800);
                    return data;
                }
                userStore.data.accessToken = data.data;
                userStore.save();
                onRefreshedToken(data.data);
            }
            finally {
                isRefreshingToken = false;
            }

            // 单独重播当前请求
            response.config.headers.Authorization = `Bearer ${userStore.data.accessToken}`;
            return axios(response.config);
        }
        // 重发同时发起的请求
        if (response.data.code === 401.8 && isRefreshingToken && response.config.url !== refreshTokenApi) {
            return repeatRequest(response.config, 'response');
        }
        // 不允许的跨域请求（服务器重启后丢失 allow_origin_list 数据）
        if (response.data.code === 401.9) {
            response.data.message = '请重新登录';
            userStore.clear();
            setTimeout(() => {
                location.href = '/login';
            }, 800);
        }
        return response;
    },
    (error: AxiosError) => {
        showFailToast('网络连接错误\n请联系管理员');
        return Promise.reject(error);
    }
);

export interface RequestConfig {
    url: string;
    method?: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'OPTIONS';
    params?: any;
    data?: any;
    contentType?: 'FORM' | 'JSON';
    headers?: { [key: string]: string };
    token?: string,
    tokenType?: 'Bearer';
    successCallback?: Function;
    failureCallback?: Function;
    errorCallback?: Function;
}

/**
 * 封装通用请求逻辑并设置默认值, 支持回调函数、Promise、async/await 方式调用
 * @param url 请求链接
 * @param config 配置 (默认 "GET" "FORM")
 */
async function request(config: RequestConfig) {
    const {
        url,
        method = 'GET',
        params = {},
        data = {},
        contentType = 'FORM',
        headers = {},
        token = '',
        tokenType = 'Bearer',
        successCallback,
        failureCallback,
        errorCallback
    } = config || {};

    if (method.toLocaleLowerCase() === 'GET' && Object.keys(data).length !== 0) {
        console.warn('RequestError: "GET" 方法不允许携带 "data" 参数，请检查你的配置。');
    }
    if (!('Content-Type' in headers)) {
        if (contentType === 'FORM') headers['Content-Type'] = 'multipart/form-data';
        if (contentType === 'JSON') headers['Content-Type'] = 'application/json';
    }
    if (token && tokenType === 'Bearer') {
        headers['Authorization'] = `Bearer ${token}`;
    }

    return service({ url, method, params, data, headers }).then((res: AxiosResponse) => {
        if (res.data.code === 200 && successCallback) successCallback(res.data);
        if (res.data.code !== 200 && failureCallback) failureCallback(res.data, res.data.code, url);

        return Promise.resolve(res.data);
    }).catch((err: AxiosError) => {
        if (errorCallback) errorCallback(err);

        return Promise.reject(err);
    });
}

export default request;
