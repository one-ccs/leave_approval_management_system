/**
 * 返回对象 原型
 * @param arg arg 待判断的参数
 * @returns
 */
function getPrototype(arg: any): string {
    return Object.prototype.toString.call(arg)
}
/**
 * 判断对象是否是 可迭代类型 [Array|Set|Map|Arguments|String|Typed Array|Generators]
 *
 * @param {any} arg 待判断的参数
 * @returns [true|false]
 */
function isIterable(arg: any): boolean {
    return isFunction(arg[Symbol.iterator])
}
function isComposite(arg: any): boolean {
    // 判断对象是否是 复合数据类型
    return !isBasic(arg)
}
/**
 * 判断对象是否是 基础数据类型 [Symbol|Boolean|String|Number|BigInt|Date|RegExp]
 *
 * @param {any} arg 待判断的参数
 * @returns [true|false]
 */
function isBasic(arg: any): boolean {
    return (
        isSymbol(arg) || isBoolean(arg) || isString(arg) ||
        isNumber(arg) || isBigInt(arg) || isDate(arg) ||
        isRegExp(arg)
    )
}
/**
 * 判断对象是否是 原始类型 [Null|Undefined|Symbol|Boolean|String|Number|BigInt]
 *
 * @param {any} arg 待判断的参数
 * @returns [true|false]
 */
function isPrimitive(arg: any): boolean {
    return (
        isNull(arg) || isUndefined(arg) || isSymbol(arg) ||
        isBoolean(arg) || isString(arg) ||
        isNumber(arg) || isBigInt(arg)
    )
}
/**
 * 判断对象是否是 常量 [Boolean|String|Number|BigInt]
 *
 * @param {any} arg 待判断的参数
 * @returns [true|false]
 */
function isConstant(arg: any): boolean {
    // 判断对象是否是 常量
    return (
        isBoolean(arg) || isString(arg) ||
        isNumber(arg) || isBigInt(arg)
    )
}
/**
 * 判断对象是否是 '[object HTML...Element]'
 *
 * @param {any} arg 待判断的参数
 * @returns [true|false]
 */
function isElement(arg: any): boolean {
    return /HTML\w+Element/.test(Object.prototype.toString.call(arg))
}
/**
 * 判断 arg 是否 typeof(arg) === 'object', 如: [], {} 等
 *
 * @param {any} arg 待判断的参数
 * @returns [true|false]
 */
function isTypeofObject(arg: any): boolean {
    return typeof(arg) === 'object'
}
function isObject(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object Object]'
}
function isFunction(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object Function]'
}
function isDate(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object Date]'
}
function isMap(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object Map]'
}
function isSet(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object Set]'
}
function isWeakMap(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object WeakMap]'
}
function isWeakSet(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object WeakSet]'
}
function isArray(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object Array]'
}
function isJSON(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object JSON]'
}
function isSymbol(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object Symbol]'
}
function isRegExp(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object RegExp]'
}
function isBoolean(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object Boolean]'
}
function isString(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object String]'
}
function isNumber(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object Number]'
}
function isBigInt(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object BigInt]'
}
function isNull(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object Null]'
}
function isUndefined(arg: any): boolean {
    return Object.prototype.toString.call(arg) === '[object Undefined]'
}
// isProxy, isReactive, isRef, isReadonly 为 vue 内置函数

export {
    getPrototype,
    isIterable,
    isComposite,
    isBasic,
    isPrimitive,
    isConstant,
    isElement,
    isTypeofObject,
    isObject,
    isFunction,
    isDate,
    isMap,
    isSet,
    isWeakMap,
    isWeakSet,
    isArray,
    isJSON,
    isSymbol,
    isRegExp,
    isBoolean,
    isString,
    isNumber,
    isBigInt,
    isNull,
    isUndefined,
}
