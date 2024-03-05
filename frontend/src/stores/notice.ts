import { defineStore } from "pinia";

const useNoticeStore = defineStore('notice', {
    state: () => ({
        systemNotice: '暂无通知',
        schoolNotice: '暂无通知',
        collegeNotice: '暂无通知',
        teacherNotice: '暂无通知',
    }),
    getters: {
    },
    actions: {
    }
});

export default useNoticeStore;
