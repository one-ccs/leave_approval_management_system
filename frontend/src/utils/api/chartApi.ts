import { api } from '.';


export function apiChartLeaveState(successCallback?: Function, failureCallback?: Function) {
    return api({
        url: '/chart/leaveState',
        successCallback,
        failureCallback,
    });
};

export function apiChartLeaveCount(successCallback?: Function, failureCallback?: Function) {
    return api({
        url: '/chart/leaveCount',
        successCallback,
        failureCallback,
    });
};

export function apiChartLeaveRank(successCallback?: Function, failureCallback?: Function) {
    return api({
        url: '/chart/leaveRank',
        successCallback,
        failureCallback,
    });
};
