const map = {
    admin: '管理员',
    teacher: '辅导员',
    student: '学生',
    管理员: 'admin',
    辅导员: 'teacher',
    学生: 'student',
    a: {
        b: {
            c: 'ccc',
        }
    }
};

export default (key: string) => {
    return key.split('.').reduce((o: any, i: string) => {
        if (o) return o[i];
    }, map);
};
