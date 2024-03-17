from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 获取元素的其他信息
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
# 打印元素的信息
print("在WebDriver实例中找到此元素的内部引用：{}".format(ele1.parent))
print("包含元素大小和位置的字典：{}".format(ele1.rect))
print("元素的大小：{}".format(ele1.size))
print("获取元素的tagname属性：{}".format(ele1.tag_name))
print("获取元素的文本值：{}".format(ele1.text))
# 休眠1秒
sleep(1)
driver.quit()