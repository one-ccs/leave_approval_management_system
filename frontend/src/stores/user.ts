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
        setUser(user: any) {
            const { avatar, name, username, role, major } = user;
            this.avatar = avatar || this.avatar;
            this.name = name || username || this.name;
            this.role = role || this.role;
            this.major = major;
        },
    }
});

export default useUserStore;
