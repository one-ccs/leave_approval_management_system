export function localLoad(key: string, def: any = null) {
    let data = localStorage.getItem(key);

    if(!data) return def;
    try {
        data = JSON.parse(data);
    }
    catch {
        // 值是普通字符串, 捕获错误
    }
    return data;
}
export function localSave(key: string, value: any) {
    localStorage.setItem(key, JSON.stringify(value));
}
export function localRemove(key: string) {
    localStorage.removeItem(key);
}
export function localClear() {
    localStorage.clear();
}

export function sessionLoad(key: string, def: any = null) {
    let data = sessionStorage.getItem(key);

    if(!data) return def;
    try {
        data = JSON.parse(data);
    }
    catch {
        // 值是普通字符串, 捕获错误
    }
    return data;
}
export function sessionSave(key: string, value: any) {
    sessionStorage.setItem(key, JSON.stringify(value));
}
export function sessionRemove(key: string) {
    sessionStorage.removeItem(key);
}
export function sessionClear() {
    sessionStorage.clear();
}
