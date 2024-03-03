import { defineStore } from "pinia";

const useGlobalStore = defineStore('global', {
    state: () => ({
        _badges: {
            notice: 0,
            app: 0,
            user: 0,
            leave: 0,
            revoke: 0,
        },
        backgroundImages: [
            '/static/img/bg/blob-scene-haikei.svg',
            '/static/img/bg/blurry-gradient-haikei.svg',
            '/static/img/bg/circle-scatter-haikei.svg',
            '/static/img/bg/layered-peaks-haikei.svg',
            '/static/img/bg/stacked-steps-haikei.svg',
            '/static/img/bg/stacked-waves-haikei.svg',
            '/static/img/bg/wave-haikei.svg',
        ],
        backgroundImageIndex: 5,
    }),
    getters: {
        badges: (state: any) => ({
            notice: state._badges.notice || '',
            app: state._badges.app || '',
            user: state._badges.user || '',
            leave: state._badges.leave || '',
            revoke: state._badges.revoke || '',
        }),
        backgroundImage: (state: any) => state.backgroundImages[state.backgroundImageIndex]
            || state.backgroundImages[0],
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
        setLeaveBadge(value: number) {
            this._badges.leave = value;
        },
        setRevokeBadge(value: number) {
            this._badges.revoke = value;
        },
        setBackgroundImageIndex(index: number) {
            this.backgroundImageIndex = index;
        },
    }
});

export default useGlobalStore;
