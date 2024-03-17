from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# get_screenshot_as_file，截屏并保存为文件
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.4",
  "appium:deviceName": "iPhone 14",
  "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
  # "appium:noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(5)
driver.get_screenshot_as_file('c.png')
sleep(1)
driver.quit()