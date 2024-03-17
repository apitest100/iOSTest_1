from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 找不到元素立即报错
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14",
  "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
  # "appium:noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
sleep(1)
# 故意输入一个错误的ACCESSIBILITY_ID值
ele1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Alert Views False')
# 点击
ele1.click()
# 休眠1秒
sleep(1)
driver.quit()
