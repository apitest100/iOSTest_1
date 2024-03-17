from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 获取元素text
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14",
  "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
  "appium:noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
sleep(1)
# 通过ACCESSIBILITY_ID定位元素Alert Views
ele1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Alert Views')
# 获取元素text
print("ele1的text是：{}".format(ele1.text))
# 休眠1秒
sleep(1)
driver.quit()
