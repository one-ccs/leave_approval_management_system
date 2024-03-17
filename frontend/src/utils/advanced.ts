export function getCurrentPosition(successCallback: PositionCallback, errorCallback?: PositionErrorCallback, options?: PositionOptions) {
    navigator.geolocation?.getCurrentPosition(successCallback, errorCallback, options);
}
