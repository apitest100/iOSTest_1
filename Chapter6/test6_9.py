from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 通过OS_PREDICATE定位Alert views，并点击
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14",
  "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
  "appium:noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(10)
sleep(1)
# find_elements()返回值是元素对象列表
elements = driver.find_elements(AppiumBy.IOS_PREDICATE, 'label ENDSWITH "Views"')
# 打印返回值类型
print(type(elements))
# 打印找到的元素数量
print(len(elements))
# 点击第一个元素，下标从0开始
elements[0].click()
# 休眠1秒
sleep(1)
driver.quit()
