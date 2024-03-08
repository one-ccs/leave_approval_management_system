import i18n from "@/utils/i18n";
import { localLoad, localRemove, localSave } from "@/utils/storage";
import { defineStore } from "pinia";

const useUserStore = defineStore('user', {
    state: () => ({
        isInit: false,
        isLogin: false,
        userInfo: {
            avatar: '/static/img/avatar.jpg',
            name: '小哆啦',
            role: '学生',
            major: '20计算机科学与技术20班',
            expires: <null | number>null,
        },
        _keyName: 'user',
    }),
    getters: {
        isExpires: (state: any) => (state.userInfo.expires <= new Date().getTime()),
    },
    actions: {
        init() {
            if (this.isInit) return this;
            this.isInit = true;

            this.load();
            return this;
        },
        load() {
            const localUser = localLoad(this._keyName);
            if (localUser) {
                this.isLogin = true;
                this.userInfo = localUser;
            }
            return this;
        },
        save() {
            localSave(this._keyName, this.userInfo);
            return this;
        },
        clear() {
            localRemove(this._keyName);
            this.isLogin = false;
            return this;
        },
        setUser(user: any) {
            const { avatar, name, username, role, major } = user;
            this.userInfo.avatar = avatar || this.userInfo.avatar;
            this.userInfo.name = name || username || this.userInfo.name;
            this.userInfo.role = i18n(role, 'roleZh') || this.userInfo.role;
            this.userInfo.major = major;
            this.userInfo.expires = ((new Date()).getTime() + 1000 * 3600 * 24);
            this.isLogin = true;
            return this;
        },
    }
});

export default useUserStore;
