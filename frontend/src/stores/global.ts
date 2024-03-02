import { defineStore } from "pinia";

const useGlobalStore = defineStore('global', {
    state: () => ({
        _badges: {
            notice: 0,
            app: 0,
            user: 0,
        }
    }),
    getters: {
        badges: (state: any) => ({
            notice: state._badges.notice ? state._badges.notice: '',
            app: state._badges.app ? state._badges.app : '',
            user: state._badges.user ? state._badges.user : '',
        }),
    },
    actions: {
        setNoticeBadge(value: number) {
            this._badges.notice = value;
        },
        setAppBadge(value: number) {
            this._badges.app = value;
        },
        setUserBadge(value: number) {
            this._badges.user = value;
        },
    }
});

export default useGlobalStore;
