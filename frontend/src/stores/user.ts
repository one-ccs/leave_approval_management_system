import { defineStore } from "pinia";

const useUserStore = defineStore('user', {
    state: () => ({
        avatar: '/static/img/avatar.jpg',
        name: '小哆啦',
        roles: [],
        role: '学生',
        major: '20计算机科学与技术20班',
    }),
    getters: {
    },
    actions: {
    }
});

export default useUserStore;
