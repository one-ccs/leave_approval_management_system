export interface User {
    avatar?: string;
    createDatetime: string;
    id: number;
    passwordHash: string;
    role: number;
    username: string;
}


export interface Admin {
    gender: string;
    id: number;
    name: string;
    userId: number;
}

export interface Teacher {
    gender: string;
    id: number;
    name: string;
    telephone: string;
    userId: number;
}

export interface Student {
    class: string;
    department: string;
    faculty: string;
    gender: string;
    grade: string;
    id: number;
    major: string;
    name: string;
    teacherId: number;
    userId: number;
}

export interface Leave {
    a1Datetime: string;
    a2Datetime: string;
    annexUrl: string;
    applyDatetime: string;
    approver1Id: number;
    approver2Id: number;
    category: string;
    endDatetime: string;
    id: number;
    leaveReason: string;
    rejectReason: string;
    revokeId: number;
    revokeDatetime: string;
    startDatetime: string;
    state: number;
    userId: number;
};
