from appium import webdriver
from time import sleep


# 向下滑动屏幕
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.4",
  "appium:deviceName": "iPhone 14",
  "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
  # "appium:noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(5)
driver.execute_script('mobile: scroll', {'direction': 'down'})
# driver.execute_scriptt('mobile: swipe', {'direction': 'up'})
sleep(2)
driver.quit()