import { localLoad, localRemove, localSave } from "@/utils/storage";
import { defineStore } from "pinia";

const useGlobalStore = defineStore('global', {
    state: () => ({
        isInit: false,
        keyName: 'globalStore',
        data: {
            version: '0.0.1',
            backgroundImageIndex: 6,
        },
        isUpdate: false,
        apiHost: 'http://127.0.0.1:5001/api',
        defaultAvatarUrl: '/static/img/avatar.jpg',
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
        version: (state: any) => state.data.version,
        backgroundImage: (state: any) => state.backgroundImages[state.data.backgroundImageIndex]
            || state.backgroundImages[0],
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
                // 利用对象展开运算符 保持响应式状态
                this.data = { ...persistence };
            }
            return this;
        },
        save() {
            localSave(this.keyName, this.data);
            return this;
        },
        clear() {
            localRemove(this.keyName);
            return this;
        },
        setBackgroundImageIndex(index: number) {
            this.data.backgroundImageIndex = index;
        },
    }
});

export default useGlobalStore;
