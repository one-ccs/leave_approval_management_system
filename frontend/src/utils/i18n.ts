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
                2: '审批中',
                3: '已驳回',
                4: '待销假',
                5: '销假中',
                6: '已完成',
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
                    title: '审批中',
                    value: 2,
                },
                {
                    title: '已驳回',
                    value: 3,
                },
                {
                    title: '已完成',
                    value: 6,
                },
            ],
            revoke: [
                {
                    title: '待销假',
                    value: 4,
                },
                {
                    title: '销假中',
                    value: 5,
                },
            ],
            history: [
                {
                    title: '待审批',
                    value: 0,
                },
                {
                    title: '已撤回',
                    value: 1,
                },
                {
                    title: '审批中',
                    value: 2,
                },
                {
                    title: '已驳回',
                    value: 3,
                },
                {
                    title: '待销假',
                    value: 4,
                },
                {
                    title: '销假中',
                    value: 5,
                },
                {
                    title: '已完成',
                    value: 6,
                },
            ],
            approve: [
                {
                    title: '待审批',
                    value: 0,
                },
                {
                    title: '二审中',
                    value: 2,
                },
                {
                    title: '已驳回',
                    value: 3,
                },
                {
                    title: '待销假',
                    value: 4,
                },
                {
                    title: '销假中',
                    value: 5,
                },
                {
                    title: '已完成',
                    value: 6,
                },
            ],
            approve2: [
                {
                    title: '待审批',
                    value: 2,
                },
                {
                    title: '已驳回',
                    value: 3,
                },
                {
                    title: '待销假',
                    value: 4,
                },
                {
                    title: '销假中',
                    value: 5,
                },
                {
                    title: '已完成',
                    value: 6,
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
        primary: '#1989FA',
        success: '#07C160',
        default: '#c2c2c2',
        warning: '#FF976A',
        danger:  '#EE0A24',
    }
};



/**
 * 返回 map 路径中查找到的值, 没有返回默认值
 * @param key 键名
 * @param path 路径 (以英文句号 . 分隔)
 * @param _default 默认值
 * @returns
 */
export default function(key: string | number, path?: string, _default: any = null) {
    if (path) key = `${path}.${key}`;
    return String(key).split('.').reduce((o: any, i: string) => o && o[i], map) || _default;
}
