from appium import webdriver
from time import sleep


# 将App切换到后台
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14",
  "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
# 等待3秒
sleep(3)
# background_app()，将App切换到后台3秒，3秒结束后，返回前台
driver.background_app(3)
sleep(3)
driver.quit()
