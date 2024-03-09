const map = {
    role: {
        zh: {
            '9': '管理员',
            '1': '辅导员',
            '0': '学生',
        },
        en: {
            '9': 'admin',
            '1': 'teacher',
            '0': 'student',
        },
    },
    leave: {
        state: {
            '0': '待审批',
            '1': '已撤回',
            '2': '已驳回',
            '3': '已完成',
        },
        category: {
            '0': '事假',
            '1': '病假',
            '2': '公假',
            '3': '出校申请',
        },
    },
};

export default (key: string | number, path?: string) => {
    if (path) key = `${path}.${key}`;
    return String(key).split('.').reduce((o: any, i: string) => o[i], map);
};
