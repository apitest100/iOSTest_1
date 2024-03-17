from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 获取元素在页面中的横纵坐标
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
# 打印“Alert Views”元素在页面中的坐标
print("获取元素在页面中的位置(方法一）：{}".format(ele1.location))
print("获取元素在页面中的位置（方法二）：{}".format(ele1.location_in_view))
# 休眠1秒
sleep(1)
driver.quit()
