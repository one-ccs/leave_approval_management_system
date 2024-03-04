import { defineStore } from "pinia";


const backgroundImageList = [
    '/static/img/bg/blob-scene-haikei.svg',
    '/static/img/bg/blurry-gradient-haikei.svg',
    '/static/img/bg/circle-scatter-haikei.svg',
    '/static/img/bg/layered-peaks-haikei.svg',
    '/static/img/bg/stacked-steps-haikei.svg',
    '/static/img/bg/stacked-waves-haikei.svg',
    '/static/img/bg/wave-haikei.svg',
];
const useGlobalStore = defineStore('global', {
    state: () => ({
        isUpdate: false,
        _badges: {
            notice: 1,
            user: 3,
            leave: 4,
            revoke: 5,
            approve: 6,
        },
        backgroundImageIndex: 5,
    }),
    getters: {
        badges: (state: any) => ({
            notice: state._badges.notice || '',
            app: state._badges.leave + state._badges.revoke + state._badges.approve || '',
            user: state.isUpdate ? state._badges.user + 1 : state._badges.user || '',
            leave: state._badges.leave || '',
            revoke: state._badges.revoke || '',
            approve: state._badges.approve || '',
        }),
        backgroundImage: (state: any) => backgroundImageList[state.backgroundImageIndex]
            || backgroundImageList[0],
    },
    actions: {
        setNoticeBadge(value: number) {
            this._badges.notice = value;
        },
        setUserBadge(value: number) {
            this._badges.user = value;
        },
        setLeaveBadge(value: number) {
            this._badges.leave = value;
        },
        setRevokeBadge(value: number) {
            this._badges.revoke = value;
        },
        setApproveBadge(value: number) {
            this._badges.approve = value;
        },
        setBackgroundImageIndex(index: number) {
            this.backgroundImageIndex = index;
        },
    }
});

export default useGlobalStore;
