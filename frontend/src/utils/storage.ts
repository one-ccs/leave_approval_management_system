function localLoad(key: string, def=null) {
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
function localSave(key: string, value: any) {
    localStorage.setItem(key, JSON.stringify(value));
}
function localRemove(key: string) {
    localStorage.removeItem(key);
}
function localClear() {
    localStorage.clear();
}

function sessionLoad(key: string, def=null) {
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
function sessionSave(key: string, value: any) {
    sessionStorage.setItem(key, JSON.stringify(value));
}
function sessionRemove(key: string) {
    sessionStorage.removeItem(key);
}
function sessionClear() {
    sessionStorage.clear();
}

export {
    localLoad,
    localSave,
    localRemove,
    localClear,
    sessionLoad,
    sessionSave,
    sessionRemove,
    sessionClear,
}
