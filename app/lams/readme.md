# 请假审批管理系统 App

## 一、环境配置

### 1、JDK

1. 环境变量
   * JAVA_HOME
   * %JAVA_HOME%\bin

### 2、Android SDK

1. 环境变量
   * ANDROID_HOME
   * ANDROID_SDK_ROOT
   * %ANDROID_HOME%\build-tools
   * %ANDROID_HOME%\tools
   * %ANDROID_HOME%\platform-tools

### 3、Node

1. 环境变量
   * ...\nodejs\node_global
2. 全局安装 Cordova
   ```powershell
   npm i -g cordova
   ```

### 4、Gradle（选装）

1. 环境变量
   * GRADLE_HOME
   * %GRADLE_HOME%\bin

## 二、项目初始化

注：在 cmd 中使用 cordova 命令，powershell 中使用 cordova.cmd 命令。

### 1、创建项目

cordova create <目录名> [根域名.公司名.项目名] [应用名称]

### 2、添加平台

```powershell
cordova platform add android

cordova platform add ios
```

### 3、拷贝静态资源

将现有项目的 index.html 及其它资源复制到 Cordova 项目的 www 文件夹中

### 4、【可选】验证环境

```powershell
cordova requirements
```

### 5、【可选】编译为 Android App

```powershell
cordova build android
```

### 6、运行（会自动编译后运行）

```powershell
cordova run android
```

## 三、问题

Q：No Java files found that extend CordovaActivity.

A：重新安装平台

```powershell
cordova platform rm android

cordova platform add android
```
