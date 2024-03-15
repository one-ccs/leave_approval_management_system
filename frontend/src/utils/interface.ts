export interface ResultData {
    code: number;
    message: string;
    data: any;
};

export interface PageQuery {
    pageIndex: number;
    pageSize: number;
    query?: string;
};

export interface LeavePageQuery extends PageQuery {
    state: number;
    category: number;
};

export interface User {
    id: number;
    username: string;
    passwordHash: string;
    role: number;
    avatar?: string;
    createDatetime: string;
};

export interface Admin {
    id: number;
    userId: number;
    name: string;
    gender: string;
};

export interface Teacher {
    id: number;
    userId: number;
    name: string;
    gender: string;
    telephone: string;
};

export interface Student {
    id: number;
    userId: number;
    teacherId: number;
    name: string;
    gender: string;
    department: string;
    faculty: string;
    major: string;
    grade: string;
    _class: string;
};

export interface Leave {
    id: number;
    userId: number;
    state: number;
    category: string;
    applyDatetime: string;
    startDatetime: string;
    endDatetime: string;
    leaveReason: string;
    annexUrl: string;
    a1Datetime: string;
    approver1Id: number;
    a2Datetime: string;
    approver2Id: number;
    revokeDatetime: string;
    revokeId: number;
    rejectReason: string;
};

export enum LeaveState {
    PENDING,      /* 待审批 */
    WITHDRAWN,    /* 已撤回 */
    REJECTED,     /* 已驳回 */
    CANCEL,       /* 待销假 */
    CANCELING,    /* 销假中 */
    DONE,         /* 已完成 */
};

export enum LeaveCategory {
    PERSONAL,     /* 事假 */
    SICK,         /* 病假 */
    PUBLIC,       /* 公假 */
    LEAVE_SCHOOL, /* 出校申请 */
};