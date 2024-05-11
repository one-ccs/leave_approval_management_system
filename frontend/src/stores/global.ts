import { defineStore } from "pinia";
import axios from "axios";
import type { NoticeExtra } from "@/utils/interface";
import { localLoad, localRemove, localSave } from "@/utils/storage";


// 测试 api 服务器是否连通
const testApi = (apiHost: string, xOriginToken: string) => axios.get(apiHost, {
    headers: {
        'X-Origin-Token': xOriginToken,
    },
});

const useGlobalStore = defineStore('global', {
    state: () => ({
        isInit: false,
        keyName: 'globalStore',
        data: {
            version: '0.0.1',
            backgroundImageIndex: 6,
        },
        isUpdate: false,
        _apiHostList: [
            'http://127.0.0.1:5001/api',
            'http://192.168.137.1:5001/api'
        ],
        apiHost: 'https://www.one-ccs.com:5001/api',
        xOriginToken: 'f0d8f7aa144828d60106968a6067ea19dbfa0d2d2e067eda19dbfa0d2d2e235d37e5198842dca67e13a',
        timeout: 5000,
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
        noticeList: <NoticeExtra[]>[],
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
            this.connectApiServer();

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
        async connectApiServer() {
            for (let apiHost of this._apiHostList) {
                try {
                    const data = await testApi(apiHost, this.xOriginToken);

                    if (data.data) {
                        this.apiHost = apiHost;
                        break;
                    }
                }
                catch(e) {}
            }
        },
        setBackgroundImageIndex(index: number) {
            this.data.backgroundImageIndex = index;
        },
    }
});

export default useGlobalStore;
