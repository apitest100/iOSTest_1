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
# Alert Views的有效点击坐标(150, 150)
x = driver.get_window_size()['width']*150/390
y = driver.get_window_size()['height']*150/840
elements = driver.tap([(x, y)], 500)
# 休眠1秒
sleep(1)
driver.quit()
