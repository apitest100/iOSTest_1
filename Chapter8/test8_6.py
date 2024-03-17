from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 隐藏软键盘，判断键盘是否显示
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.4",
  "appium:deviceName": "iPhone 14",
  "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
  # "appium:noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Text Fields').click()
driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "Placeholder text"`][1]').click()
sleep(2)
driver.hide_keyboard()
sleep(2)
print(driver.is_keyboard_shown())
driver.quit()