from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


# TouchAction操作，tap坐标点
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
# 定位第一个文本输入框
ele2 = driver.find_elements(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextField"')[0]
# long_press需要传递两个参数，一个是目标元素，一个是长按的时间，单位为微秒
ele2.send_keys('storm')
sleep(2)
# 注意，长按后，需要先使用release释放按键，再使用perform执行
TouchAction(driver).long_press(ele2, 3000).release().perform()
sleep(3)
driver.quit()
