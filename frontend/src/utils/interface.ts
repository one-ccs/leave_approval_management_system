/* --------- po --------- */

export interface User {
    id: number;
    username: string;
    passwordHash: string;
    email: string;
    role: number;
    avatar: string;
    createDatetime: string;
};

export interface Admin {
    id: number;
    userId: number;
    name: string;
    gender: string;
    telephone: string;
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
    state: ELeaveState;
    category: ELeaveCategory;
    applyDatetime: string;
    startDatetime: string;
    endDatetime: string;
    duration: number;
    leaveReason: string;
    annexUrl: string;
    cancelDatetime: string;
    revokeDatetime: string;
    revokeLongitude: number;
    revokeLatitude: number;
    approver1Id: number;
    a1Datetime: string;
    approver2Id: number;
    a2Datetime: string;
    revokeId: number;
    rejectDatetime: string;
    rejectReason: string;
};

export interface Notice {
    id: number;
    userId: number;
    title: string;
    content: string;
    releaseDatetime: string;
};

export type RoleEn = 'student' | 'teacher' | 'admin';

export enum ERole {
    admin = 9,
    teacher = 1,
    student = 0,
};

export enum ELeaveState {
    PENDING,      /* 待审批 */
    WITHDRAWN,    /* 已撤回 */
    APPROVING,    /* 审批中 */
    REJECTED,     /* 已驳回 */
    CANCEL,       /* 待销假 */
    CANCELING,    /* 销假中 */
    DONE,         /* 已完成 */
};

export enum ELeaveCategory {
    PERSONAL,     /* 事假 */
    SICK,         /* 病假 */
    PUBLIC,       /* 公假 */
    LEAVE_SCHOOL, /* 出校申请 */
};

/* --------- dto --------- */

export interface UnionUser extends User, Admin, Teacher, Student {
    name: string;
    teacherName: string;
    admissionDate: string;
    school: string;
    expires: number | null;
};

/* --------- vo --------- */

export interface ResponseData {
    code: number;
    message: string;
    data: any;
};

export interface PageQuery {
    pageIndex: number;
    pageSize: number;
    query?: string;
};

export interface TimeRangePageQuery extends PageQuery {
    startDatetime: string;
    endDatetime: string;
};

export interface LeavePageQuery extends PageQuery {
    state: number;
    category: number;
};

export interface LoginUser {
    username: string;
    email?: string;
    password: string;
    captcha?: string;
    remember: boolean;
};

export interface LeaveAddForm {
    category: number;
    startDatetime: string;
    endDatetime: string;
    leaveSchool: boolean;
    leaveReason: string;
};
