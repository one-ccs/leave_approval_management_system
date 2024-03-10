import { localLoad, localRemove, localSave } from "@/utils/storage";
import { defineStore } from "pinia";

const useGlobalStore = defineStore('global', {
    state: () => ({
        isInit: false,
        isUpdate: false,
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
        _persistence: {
            version: '0.0.1',
            backgroundImageIndex: 6,
        },
        _keyName: 'globalStore',
    }),
    getters: {
        version: (state: any) => state._persistence.version,
        backgroundImage: (state: any) => state.backgroundImages[state._persistence.backgroundImageIndex]
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
            const persistence = localLoad(this._keyName);
            if (persistence) {
                // 利用对象展开运算符 保持响应式状态
                this._persistence = { ...persistence };
            }
            return this;
        },
        save() {
            localSave(this._keyName, this._persistence);
            return this;
        },
        clear() {
            localRemove(this._keyName);
            return this;
        },
        setBackgroundImageIndex(index: number) {
            this._persistence.backgroundImageIndex = index;
        },
    }
});

export default useGlobalStore;
