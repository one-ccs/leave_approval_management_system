/**
 * node 脚本，在 Android 端编译前执行的脚本，对一些文件进行特定的修改
 */
const { program } = require('commander');
const fs = require('fs');
const path = require('path');


const options = program
    .version('0.0.1')
    .option('-p | --platform <char>', '平台')
    .parse(process.argv)
    .opts();
const indexPath = path.join(__dirname, '../www/index.html');
const modifyAndroid = /* html */`
    <!-- before-build start -->
    <script src="cordova.js"></script>
    <script>
        document.addEventListener('deviceready', () => {
            // StatusBar.overlaysWebView(true);
        })
    </script>
    <style>
        #app {
            padding-top: 24px;
        }
    </style>
    <!-- before-build end -->
`;


if(options.platform === 'android') {
    fs.readFile(indexPath, 'utf8', function (err, data) {
        if (err) {
            return console.error(err);
        }

        var modifiedData = data
            .replace(/<!-- before-build start -->[\s\S]+<!-- before-build end -->\s+/, '')
            .replace('</title>', '</title>' + modifyAndroid);

        fs.writeFile(indexPath, modifiedData, 'utf8', function (err) {
            if (err) {
                return console.error(err);
            }
            console.log('[BEFORE_BUILD] - 修改成功 (Android)');
        });
    });
}
