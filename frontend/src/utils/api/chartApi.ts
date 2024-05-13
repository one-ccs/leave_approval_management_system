import { api } from '.';


export function apiChartLeaveState(duration: number, successCallback?: Function, failureCallback?: Function) {
    return api({
        url: '/chart/leaveState',
        params: {
            duration,
        },
        successCallback,
        failureCallback,
    });
};

export function apiChartLeaveCount(duration: number, successCallback?: Function, failureCallback?: Function) {
    return api({
        url: '/chart/leaveCount',
        params: {
            duration,
        },
        successCallback,
        failureCallback,
    });
};

export function apiChartLeaveRank(duration: number, successCallback?: Function, failureCallback?: Function) {
    return api({
        url: '/chart/leaveRank',
        params: {
            duration,
        },
        successCallback,
        failureCallback,
    });
};
