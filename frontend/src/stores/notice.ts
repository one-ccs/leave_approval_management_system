import { defineStore } from "pinia";

const useNoticeStore = defineStore('notice', {
    state: () => ({
        _isInit: false,
        systemNotice: '暂无通知',
        schoolNotice: '暂无通知',
        collegeNotice: '暂无通知',
        teacherNotice: '暂无通知',
    }),
    getters: {
    },
    actions: {
        init() {
            if (this._isInit) return;
            this._isInit = true;

            this.systemNotice = '暂无通知';
            this.schoolNotice = '暂无通知';
            this.collegeNotice = '暂无通知';
            this.teacherNotice = '暂无通知';
        },
    }
});

export default useNoticeStore;
