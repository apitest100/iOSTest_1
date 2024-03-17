from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 坐标点点击
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14",
  "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
  "appium:noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(10)
sleep(1)
# Alert Views的坐标大致为(100, 155)
elements = driver.tap([(100, 155)], 500)
# 休眠1秒
sleep(1)
driver.quit()
