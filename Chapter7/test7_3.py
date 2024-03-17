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
# 定位元素Text Fields，并点击
ele1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Text Fields')
ele1.click()
# 组元素定位
ele2 = driver.find_elements(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextField"')
ele2[0].send_keys('Storm')
# 休眠1秒
sleep(1)
# 假设使用test7_2.py中xpath的定位方式，则此处清除不成功
ele2[0].clear()
sleep(1)
driver.quit()
