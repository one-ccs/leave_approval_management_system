const map = {
    roleZh: {
        0: '管理员',
        1: '辅导员',
        2: '学生',
    },
    roleEn: {
        0: 'admin',
        1: 'teacher',
        2: 'student',
    },
};

export default (key: string | number, path?: string) => {
    if (path) key = `${path}.${key}`;
    return String(key).split('.').reduce((o: any, i: string) => o[i], map);
};
