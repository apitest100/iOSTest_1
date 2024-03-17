from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 点击操作
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14",
  "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
  # "appium:noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
sleep(1)
# 定位元素
ele = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Alert Views')
# click(),方法用于实现左键点击效果
ele.click()
# 休眠1秒
sleep(1)
driver.quit()
