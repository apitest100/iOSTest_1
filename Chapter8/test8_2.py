from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


# TouchAction操作，tap目标元素
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.4",
  "appium:deviceName": "iPhone 14",
  "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
  # "appium:noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(5)
ele1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Text Fields')
# 可以传递元素对象点击
TouchAction(driver).tap(ele1).perform()
sleep(3)
driver.quit()
