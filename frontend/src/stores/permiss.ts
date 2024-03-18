import { defineStore } from "pinia";

export type RoleEn = 'student' | 'teacher' | 'admin';

const usePermissStore = defineStore('permiss', {
    state: () => ({
        _role: <RoleEn>'student',
        _permiss: <{[key: string]: number[]}>{
            student: [0x100, 1, 2, 3, 4],
            teacher: [0x200, 5, 6, 7, 8],
            admin:   [0x400, 9, 10, 11, 12, 13, 14],
        },
    }),
    getters: {
        role: (state) => state._role,
        permiss: (state) => state._permiss[state._role] || state._permiss.student,
    },
    actions: {
        setRole(role: RoleEn) {
            this._role = role;
        },
        hasPermiss(permiss: number) {
            return this.permiss.includes(permiss);
        }
    }
});

export default usePermissStore;
