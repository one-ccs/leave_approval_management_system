import { defineStore } from "pinia";
import { localLoad, localRemove, localSave } from "@/utils/storage";
import i18n from "@/utils/i18n";
import usePermissStore from "./permiss";
import pinia from "./pinia";


export interface User {
    avatar: string;
    name: string;
    username: string | undefined;
    role: number;
    major: string;
    expires: number | null;
};

const permissStore = usePermissStore(pinia);

const useUserStore = defineStore('user', {
    state: () => ({
        isInit: false,
        isLogin: false,
        userInfo: <User>{
            avatar: '/static/img/avatar.jpg',
            name: '小哆啦',
            role: 2,
            major: '20计算机科学与技术20班',
            expires: null,
        },
        _keyName: 'user',
    }),
    getters: {
        role: (state: any) => state.userInfo.role,
        roleZh: (state: any) => i18n(state.userInfo.role, 'roleZh'),
        roleEn: (state: any) => i18n(state.userInfo.role, 'roleEn'),
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
                this.setUser(localUser);
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
        setUser(user: User) {
            // 设置用户信息
            const { avatar, name, username, role, major } = user;
            this.userInfo.avatar = avatar || this.userInfo.avatar;
            this.userInfo.name = name || username || this.userInfo.name;
            this.userInfo.role = role >= 0 ? role : this.userInfo.role;
            this.userInfo.major = major;
            this.userInfo.expires = ((new Date()).getTime() + 1000 * 3600 * 24);
            // 修改登录状态
            this.isLogin = true;
            // 设置用户权限
            permissStore.setRole(i18n(role, 'roleEn'));
            return this;
        },
        isExpired() {
            if (!this.userInfo.expires) return true;
            return this.userInfo.expires <= new Date().getTime();
        },
    }
});

export default useUserStore;
