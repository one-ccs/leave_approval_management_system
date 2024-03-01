import axios, { type AxiosInstance, type AxiosError, type AxiosResponse, type AxiosRequestConfig } from 'axios';
import { showToast, showSuccessToast, showFailToast } from 'vant';

const service = axios.create({
    baseURL: 'http://127.0.0.1:5001',
    timeout: 5000,
    // 小于 500 的状态码不抛出错误
    validateStatus: status => (status < 500),
});

// 请求拦截器
service.interceptors.request.use(
    (config: AxiosRequestConfig) => {
        return config;
    },
    (error: AxiosError) => {
        return Promise.reject();
    }
);

// 响应拦截器
service.interceptors.response.use(
    (response: AxiosResponse) => {
        // 未登录，或登录已过期
        if (response.data.code === 401) {
            showToast('未登录，即将跳转登录页...');
            setTimeout(() => {
                location.href = '/login';
            }, 1200);
        }
        return response;
    },
    (error: AxiosError) => {
        showFailToast('发生了一些错误，请联系管理员。')
        return Promise.reject();
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
        if (res.data.code === 200 && success) return Promise.resolve(success(res.data));
        if (res.data.code !== 200 && failure) return Promise.resolve(failure(res.data, res.data.code, url));

        return Promise.resolve(res.data);
    }).catch((err: AxiosError) => {
        if (error) return Promise.reject(error(err));

        return Promise.reject(err);
    });
}

export default request;
