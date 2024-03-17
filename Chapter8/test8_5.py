from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction


# TouchAction操作，多点触控----放大效果
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.3.1",
  "appium:deviceName": "iPhone 12",
  "appium:udid": "00008101-000B64AE3C98001E",
  "bundleId": "com.dangdang.iphone",
  "appium:noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(10)

# ele1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Text Fields')

# 获取窗口的长和宽
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
# 缩小效果
action1 = TouchAction(driver)  # 第一个手势
action2 = TouchAction(driver)  # 第二个手势
pinch_action = MultiAction(driver)

action1.press(x=x * 0.2, y=y * 0.2).wait(1000).move_to(x=x * 0.4, y=y * 0.4).release()
action2.press(x=x * 0.8, y=y * 0.8).wait(1000).move_to(x=x * 0.6, y=y * 0.6).release()
pinch_action.add(action1, action2)  # 加载
pinch_action.perform()  # 执行


sleep(3)
driver.quit()
