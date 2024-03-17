from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 判断原始是否可见、可用、被选中
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14",
  "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
  # "appium:noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
sleep(1)
# 定位元素Alert Views，并点击
ele1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Alert Views')
# 判断元素是否可见
print(ele1.is_displayed())
# 判断元素是否可用
print(ele1.is_enabled())
# 判断元素是否选中
print(ele1.is_selected())
# 休眠1秒
sleep(1)
driver.quit()
