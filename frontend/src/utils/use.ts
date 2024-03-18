import { ELeaveState } from "./interface";
import i18n from "./i18n";


/**
 * 返回开始时间到结束时间持续的天数
 * @param startDatetime 开始日期时间
 * @param endDatetime 结束日期时间
 * @returns 持续的天数向上取整
 */
export function useLeaveDuration(startDatetime: string, endDatetime: string) {
    return Math.ceil(
        (new Date(endDatetime).getTime()
        - new Date(startDatetime).getTime())
        / 3600 / 1000 / 24
    );
}

/**
 * 返回状态值对应的颜色
 * @param state 状态值
 * @returns 十六进制颜色值
 */
export function useStateColor(state: number) {
    switch(state){
        case ELeaveState.PENDING:
        case ELeaveState.WITHDRAWN:
            return i18n('color.default');
        case ELeaveState.REJECTED:
            return i18n('color.danger');
        case ELeaveState.APPROVING:
            return i18n('color.primary')
        case ELeaveState.CANCEL:
        case ELeaveState.CANCELING:
            return i18n('color.warning');
        case ELeaveState.DONE:
            return i18n('color.success');
    }
};
