import { showLoadingToast, showSuccessToast, showFailToast } from "vant";
import { defineStore } from "pinia";
import axios from "axios";
import type { LeaveExtra, NoticeExtra } from "@/utils/interface";
import { useDynamicAssets } from "@/utils/use";
import { localLoad, localRemove, localSave } from "@/utils/storage";


// 测试 api 服务器是否连通
const testApi = (apiHost: string, xOriginToken: string) => axios.get(apiHost, {
    headers: {
        'X-Origin-Token': xOriginToken,
    },
    timeout: 3000,
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
            'http://192.168.137.1:5001/api',
            'http://192.168.37.1:5001/api',
            'http://192.168.71.106:5001/api',
        ],
        apiHost: 'https://www.one-ccs.com:5001/api',
        onConnectedServer: (apiHost: string) => {},
        xOriginToken: 'f0d8f7aa144828d60106968a6067ea19dbfa0d2d2e067eda19dbfa0d2d2e235d37e5198842dca67e13a',
        timeout: 5000,
        defaultAvatarUrl: useDynamicAssets('images/avatar.jpg'),
        logoPngUrl: useDynamicAssets('images/logo.png'),
        backgroundImages: [
            useDynamicAssets('images/bg/blob-scene-haikei.svg'),
            useDynamicAssets('images/bg/blurry-gradient-haikei.svg'),
            useDynamicAssets('images/bg/circle-scatter-haikei.svg'),
            useDynamicAssets('images/bg/layered-peaks-haikei.svg'),
            useDynamicAssets('images/bg/layered-waves-haikei.svg'),
            useDynamicAssets('images/bg/stacked-steps-haikei.svg'),
            useDynamicAssets('images/bg/stacked-waves-haikei.svg'),
            useDynamicAssets('images/bg/wave-haikei.svg'),
        ],
        leaveList: <LeaveExtra[]>[],
        noticeList: <NoticeExtra[]>[],
    }),
    getters: {
        version: (state: any): string => state.data.version,
        backgroundImage: (state: any): URL => state.backgroundImages[state.data.backgroundImageIndex]
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
            const toast = showLoadingToast({
                type: 'loading',
                message: `正在尝试连接\n服务器...`,
                overlay: true,
                forbidClick: false,
                duration: 0,
            });
            let isSuccess = false, i = 0;

            for (let apiHost of this._apiHostList) {
                toast.message = `正在尝试连接\n服务器：${++i}`;

                try {
                    const data = await testApi(apiHost, this.xOriginToken);

                    if (data.data) {
                        isSuccess = true;
                        this.apiHost = apiHost;
                        this.onConnectedServer(apiHost);
                        break;
                    }
                }
                catch(e) {}
            }
            isSuccess ? showSuccessToast('服务器连接\n成功') : showFailToast('服务器连接\n失败');
        },
        setBackgroundImageIndex(index: number) {
            this.data.backgroundImageIndex = index;
        },
    }
});

export default useGlobalStore;
