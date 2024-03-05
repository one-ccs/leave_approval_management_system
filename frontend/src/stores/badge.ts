import { defineStore } from "pinia";

const useBadgeStore = defineStore('badge', {
    state: () => ({
        _notice: 1,
        _user: 3,
        _leave: 4,
        _revoke: 5,
        _approve: 6,
    }),
    getters: {
        notice: (state: any) => state._notice || '',
        app: (state: any) => state._leave + state._revoke + state._approve || '',
        user: (state: any) => state.isUpdate ? state._user + 1 : state._user || '',
        leave: (state: any) => state._leave || '',
        revoke: (state: any) => state._revoke || '',
        approve: (state: any) => state._approve || '',
    },
    actions: {
        setNoticeBadge(value: number) {
            this._notice = value;
        },
        setUserBadge(value: number) {
            this._user = value;
        },
        setLeaveBadge(value: number) {
            this._leave = value;
        },
        setRevokeBadge(value: number) {
            this._revoke = value;
        },
        setApproveBadge(value: number) {
            this._approve = value;
        },
    }
});

export default useBadgeStore;
