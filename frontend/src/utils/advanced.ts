import { showFailToast } from "vant";


function defaultPositionErrorCallback<PositionErrorCallback>(error: { code: number, message: string }) {
    if (error.code === 1) showFailToast('操作失败\n没有定位权限');
}

export function getCurrentPosition(successCallback: PositionCallback, errorCallback: PositionErrorCallback = defaultPositionErrorCallback, options?: PositionOptions) {
    navigator.geolocation?.getCurrentPosition(successCallback, errorCallback, options);
}
