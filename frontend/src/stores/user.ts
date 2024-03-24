import { defineStore } from "pinia";
import type { UnionUser } from "@/utils/interface";
import { localLoad, localRemove, localSave } from "@/utils/storage";
import i18n from "@/utils/i18n";
import pinia from "./pinia";
import usePermissStore from "./permiss";
import useGlobalStore from "./global";


const permissStore = usePermissStore(pinia);
const globalStore = useGlobalStore(pinia);

const useUserStore = defineStore('user', {
    state: () => ({
        isInit: false,
        isLogin: false,
        _persistence: <UnionUser>{
            name: '小哆啦',
            role: 0,
            expires: null,
        },
        _keyName: 'userStore',
    }),
    getters: {
        role: (state: any): number => state._persistence.role,
        roleZh: (state: any):string => i18n(state._persistence.role, 'role.zh'),
        roleEn: (state: any): string => i18n(state._persistence.role, 'role.en'),
        userInfo: (state: any): UnionUser => state._persistence,
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
        setUser(user: UnionUser) {
            // 设置用户信息
            const { avatar, name, username, role, gender, _class, grade, admissionDate, createDatetime, major } = user;
            this._persistence = {
                ...user,
                role: role >= 0 ? role : this._persistence.role,
                name: name || username || this._persistence.name,
                gender: gender || '保密',
                _class: _class ? _class.length > 2 ? _class : `${grade}${major}${_class}班` : '',
                admissionDate: admissionDate || createDatetime || '',
                expires: ((new Date()).getTime() + 1000 * 3600 * 24),
            };

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
