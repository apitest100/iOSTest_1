from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 通过谓词IN定位元素
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
# 只要符合集合中的name值，就定位元素
elements = driver.find_elements(AppiumBy.IOS_PREDICATE, "name IN {'Alert Views','Buttons'}")
# for循环
# get_attribute()，用于获取元素属性值，后续讲解
for ele in elements:
    print(ele.get_attribute('name'))
# 休眠1秒
sleep(1)
driver.quit()
