import { isArray, isBasic, isPrimitive, isObject, isTypeofObject} from './typeof'


/**
 * 将 from 深拷贝到 to，使代理不丢失其响应性。只拷贝两边都存在的属性。
 * 注: to 和 from 数据类型不同也会成功拷贝，但请注意结果可能不符合预期。
 * @param {any} to 拷贝到该对象
 * @param {any} from 从该对象拷贝
 * @param {string} key 待拷贝的属性，留空递归拷贝所有属性
 * @returns None
 */
function deepCopy(to: any, from: any, key: string = '') {
    if (!isTypeofObject(to) || !isTypeofObject(from)) throw new TypeError(`参数 to(${typeof(to)}) 和 from(${typeof(from)}) 必须是 object 类型`)

    if (!key) { // 第一层
        for(let k of Object.keys(from)) { // 遍历 from
            deepCopy(to, from, k)
        }
    }
    else { // 执行拷贝
        if (isBasic(from[key]) || isPrimitive(from[key])) { // 基础/原始类型直接拷贝
            to[key] = from[key]
        }
        else { // 数组、对象等继续遍历
            // 待拷贝对象赋初值，防止属性不存在
            if(isArray(from[key])) to[key] = []
            if(isObject(from[key])) to[key] = {}
            deepCopy(to[key], from[key])
        }
    }
}

export {
    deepCopy,
}
