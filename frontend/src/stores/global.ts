import { defineStore } from "pinia";

const useGlobalStore = defineStore('global', {
    state: () => ({
        isUpdate: false,
        backgroundImageIndex: 6,
        backgroundImages: [
            '/static/img/bg/blob-scene-haikei.svg',
            '/static/img/bg/blurry-gradient-haikei.svg',
            '/static/img/bg/circle-scatter-haikei.svg',
            '/static/img/bg/layered-peaks-haikei.svg',
            '/static/img/bg/layered-waves-haikei.svg',
            '/static/img/bg/stacked-steps-haikei.svg',
            '/static/img/bg/stacked-waves-haikei.svg',
            '/static/img/bg/wave-haikei.svg',
        ],
    }),
    getters: {
        backgroundImage: (state: any) => state.backgroundImages[state.backgroundImageIndex]
            || state.backgroundImages[0],
    },
    actions: {
        setBackgroundImageIndex(index: number) {
            this.backgroundImageIndex = index;
        },
    }
});

export default useGlobalStore;
