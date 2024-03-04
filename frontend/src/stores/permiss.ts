import { defineStore } from "pinia";

type Role = 'student' | 'teacher' | 'admin';

const usePermissStore = defineStore('permiss', {
    state: () => ({
        _role: <Role>'student',
        _permiss: <{[key: string]: number[]}>{
            student: [1, 2, 3, 4],
            teacher: [5, 6, 7],
            admin: [8, 9, 10, 11, 12],
        },
    }),
    getters: {
        role: (state) => state._role,
        permiss: (state) => state._permiss[state._role],
    },
    actions: {
        setRole(role: Role) {
            this._role = role;
        },
        hasPermiss(permiss: number) {
            return this.permiss.includes(permiss);
        }
    }
});

export default usePermissStore;
