import axios, { type AxiosInstance, type AxiosError, type AxiosResponse, type InternalAxiosRequestConfig } from 'axios';
import { showFailToast } from 'vant';

const service: AxiosInstance = axios.create({
    // baseURL: 'http://127.0.0.1:5001',
    timeout: 5000,
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
        return response;
    },
    (error: AxiosError) => {
        showFailToast('发生了一些错误，请联系管理员。')
        return Promise.reject(error);
    }
);

interface RequestConfig {
    method?: 'get' | 'post' | 'put' | 'delete' | 'options';
    params?: any;
    data?: any;
    contentType?: 'form' | 'json';
    headers?: { [key: string]: string };
    token?: string,
    tokenType?: 'Bearer';
    success?: Function;
    failure?: Function;
    error?: Function;
}

/**
 * 封装通用请求逻辑并设置默认值, 支持回调函数、Promise、async/await 方式调用
 * @param url 请求链接
 * @param config 配置
 */
async function request(url: string, config?: RequestConfig) {
    let {
        method = 'GET',
        params = {},
        data = {},
        contentType = 'json',
        headers = {},
        token = '',
        tokenType = 'Bearer',
        success,
        failure,
        error
    } = (config || {});

    if (method.toLocaleLowerCase() === 'get' && Object.keys(data).length !== 0) console.error('RequestError: "GET" 方法不允许携带 "data" 参数，请检查你的配置。');
    if (!('Content-Type' in headers)) {
        if (contentType === 'form') headers['Content-Type'] = 'multipart/form-data';
        if (contentType === 'json') headers['Content-Type'] = 'application/json';
    }
    if (token && tokenType === 'Bearer') headers['Authorization'] = `Bearer ${token}`;

    return service({ url, method, params, data, headers }).then((res: AxiosResponse) => {
        if (res.data.code === 200 && success) success(res.data);
        if (res.data.code !== 200 && failure) failure(res.data, res.data.code, url);

        return Promise.resolve(res.data);
    }).catch((err: AxiosError) => {
        if (error) error(err);

        return Promise.reject(err);
    });
}

export default request;
