from appium import webdriver
from time import sleep


# 安装App，该脚本不会打开App
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14",
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.install_app("/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app")
# 休眠3秒
sleep(3)
driver.quit()
