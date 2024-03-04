import { defineStore } from "pinia";

const useUserStore = defineStore('user', {
    state: () => ({
        avatar: '/static/img/avatar.jpg',
        name: '小哆啦',
        role: '学生',
        major: '20计算机科学与技术20班',
    }),
    getters: {
    },
    actions: {
        initUser(user: any) {
            const { avatar, name, role, major } = user;
            this.avatar = avatar || this.avatar;
            this.name = name;
            this.role = role;
            this.major = major;
        }
    }
});

export default useUserStore;
