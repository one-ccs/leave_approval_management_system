const map = {
    admin: '管理员',
    teacher: '辅导员',
    student: '学生',
    管理员: 'admin',
    辅导员: 'teacher',
    学生: 'student',
    role: {
        0: '管理员',
        1: '辅导员',
        2: '学生',
    },
};

export default (key: string, path?: string) => {
    if (path) key = `${path}.${key}`;
    return key.split('.').reduce((o: any, i: string) => o[i], map);
};
