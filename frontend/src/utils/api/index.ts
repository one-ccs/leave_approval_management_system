import { showSuccessToast, showFailToast } from 'vant';
import type { ResponseData } from '../interface';


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

export * from './userApi';
export * from './adminApi';
export * from './teacherApi';
export * from './studentApi';
export * from './leaveApi';
export * from './noticeApi';
export * from './uploadApi';
