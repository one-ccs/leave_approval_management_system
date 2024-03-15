const map = {
    role: {
        zh: {
            9: '管理员',
            1: '辅导员',
            0: '学生',
        },
        en: {
            9: 'admin',
            1: 'teacher',
            0: 'student',
        },
    },
    field: {
        leave: {
            state: {
                0: '待审批',
                1: '已撤回',
                2: '已驳回',
                3: '待销假',
                4: '销假中',
                5: '已完成',
            },
            category: {
                0: '事假',
                1: '病假',
                2: '公假',
                3: '出校申请',
            },
        },
    },
    tabs: {
        state: {
            leave: [
                {
                    title: '待审批',
                    value: 0,
                },
                {
                    title: '已撤回',
                    value: 1,
                },
                {
                    title: '已驳回',
                    value: 2,
                },
                {
                    title: '已完成',
                    value: 5,
                },
            ],
            revoke: [
                {
                    title: '待销假',
                    value: 3,
                },
                {
                    title: '销假中',
                    value: 4,
                },
            ],
        },
        category: [
            {
                title: '全部类型',
                value: -1,
            },
            {
                title: '事假',
                value: 0,
            },
            {
                title: '病假',
                value: 1,
            },
            {
                title: '公假',
                value: 2,
            },
            {
                title: '出校申请',
                value: 3,
            },
        ],
    },
    color: {
        success: '#6dd080',
        danger:  '#ff8383',
        warning: '#ff9632',
        info:    '#c2c2c2',
    }
};

export default (key: string | number, path?: string) => {
    if (path) key = `${path}.${key}`;
    return String(key).split('.').reduce((o: any, i: string) => o[i], map);
};
