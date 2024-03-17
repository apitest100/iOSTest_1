from appium import webdriver
from time import sleep


# 安装App，等待3秒后，然后退出App
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14",
  "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
# 休眠3秒
sleep(3)
driver.quit()
