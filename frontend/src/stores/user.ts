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
        _persistence: <User>{
            avatar: '/static/img/avatar.jpg',
            name: '小哆啦',
            role: 2,
            major: '20计算机科学与技术20班',
            expires: null,
        },
        _keyName: 'userStore',
    }),
    getters: {
        role: (state: any) => state._persistence.role,
        roleZh: (state: any) => i18n(state._persistence.role, 'role.zh'),
        roleEn: (state: any) => i18n(state._persistence.role, 'role.en'),
        userInfo: (state: any) => state._persistence,
    },
    actions: {
        init() {
            if (this.isInit) return this;
            this.isInit = true;

            this.load();
            return this;
        },
        load() {
            const persistence = localLoad(this._keyName);
            if (persistence) {
                this.setUser(persistence);
            }
            return this;
        },
        save() {
            localSave(this._keyName, this._persistence);
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
            this._persistence.avatar = avatar || this._persistence.avatar;
            this._persistence.name = name || username || this._persistence.name;
            this._persistence.role = role >= 0 ? role : this._persistence.role;
            this._persistence.major = major;
            this._persistence.expires = ((new Date()).getTime() + 1000 * 3600 * 24);
            // 修改登录状态
            this.isLogin = true;
            // 设置用户权限
            permissStore.setRole(i18n(role, 'role.en'));
            return this;
        },
        isExpired() {
            if (!this._persistence.expires) return true;
            return this._persistence.expires <= new Date().getTime();
        },
    }
});

export default useUserStore;
