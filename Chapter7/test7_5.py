from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 获取元素id
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
# 通过IOS_CLASS_CHAIN定位元素Alert Views
ele2 = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Alert Views"`]')
# 打印id
print("ele1的id是：{}".format(ele1.id))
print("ele2的id是：{}".format(ele2.id))
print("两者是否为同一元素：", ele1.id == ele2.id)
# 休眠1秒
sleep(1)
driver.quit()
