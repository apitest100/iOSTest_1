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
# 这里不推荐使用-ios class chain
# 定位文本框，输入文字"Storm"
ele2_xpath = '//XCUIElementTypeApplication[@name="UIKitCatalog"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextField'
ele2 = driver.find_element(AppiumBy.XPATH, ele2_xpath)
# 组元素定位
# ele2 = driver.find_elements(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextField"')
# print(len(ele2))
# ele2[0].send_keys('Storm')
# 休眠1秒
sleep(1)
driver.quit()
