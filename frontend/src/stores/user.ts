import { showFailToast } from "vant";
import { defineStore } from "pinia";
import type { ResponseData, UnionUser } from "@/utils/interface";
import { localLoad, localRemove, localSave } from "@/utils/storage";
import i18n from "@/utils/i18n";
import pinia from "./pinia";
import usePermissStore from "./permiss";


const permissStore = usePermissStore(pinia);

const useUserStore = defineStore('user', {
    state: () => ({
        isInit: false,
        keyName: 'userStore',
        data: <UnionUser>{
            name: '小哆啦',
            role: 0,
        },
        isLogin: false,
    }),
    getters: {
        role: (state: any): number => state.data.role,
        roleZh: (state: any):string => i18n(state.data.role, 'role.zh'),
        roleEn: (state: any): string => i18n(state.data.role, 'role.en'),
        userInfo: (state: any): UnionUser => state.data,
    },
    actions: {
        init() {
            if (this.isInit) return this;
            this.isInit = true;

            this.load();
            return this;
        },
        load() {
            const persistence = localLoad(this.keyName);
            if (persistence) {
                this.setUser(persistence);
            }
            return this;
        },
        save() {
            localSave(this.keyName, this.data);
            return this;
        },
        clear() {
            this.$reset();
            localRemove(this.keyName);
            return this;
        },
        setUser(user: UnionUser) {
            // 设置用户信息
            const { name, username, role, gender, _class, grade, admissionDate, createDatetime, major } = user;
            this.data = {
                ...user,
                role: role >= 0 ? role : this.data.role,
                name: name || username || this.data.name,
                gender: gender || '保密',
                _class: _class ? _class.length > 2 ? _class : `${grade}${major}${_class}班` : '',
                admissionDate: admissionDate || createDatetime || '',
            };

            // 修改登录状态
            this.isLogin = true;
            // 设置用户权限
            permissStore.setRole(i18n(role, 'role.en'));
            return this;
        },
    }
});

export default useUserStore;
