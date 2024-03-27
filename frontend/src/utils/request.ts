import axios, { type AxiosInstance, type AxiosError, type AxiosResponse, type InternalAxiosRequestConfig } from 'axios';
import { showFailToast } from 'vant';
import useUserStore from '@/stores/user';
import pinia from '@/stores/pinia';


const userStore = useUserStore(pinia);


const service: AxiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:5001',
    timeout: 5000,
    // withCredentials: true
    // 设置允许携带 cookie, 否则登录后 flask.session 无法无法设置 cookie,
    // 且服务器的 Access-Control-Allow-Origin 不能设置为 '*', 需要设置白名单进行过滤
    // 且需要设置 Access-Control-Allow-Credentials: 'true'
    withCredentials: true,
    // 小于 500 的状态码不抛出错误
    validateStatus: status => (status < 500),
});

// 请求拦截器
service.interceptors.request.use(
    (config: InternalAxiosRequestConfig) => {
        return config;
    },
    (error: AxiosError) => {
        return Promise.reject(error);
    }
);

// 响应拦截器
service.interceptors.response.use(
    (response: AxiosResponse) => {
        // 未登录，或登录已过期
        if (response.data.code === 401) {
            showFailToast('未登录\n即将跳转登录页...');
            userStore.clear();
            setTimeout(() => {
                // 使用 location.href 跳转 而不是 router 防止某些情况下页面不改变的 bug
                location.href = '/login';
            }, 800);
            return response;
        }
        return response;
    },
    (error: AxiosError) => {
        showFailToast('发生了一些错误，请联系管理员。')
        return Promise.reject(error);
    }
);

export interface RequestConfig {
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
async function request(url: string, config?: RequestConfig) {
    let {
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
