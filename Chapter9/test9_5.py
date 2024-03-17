from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep


# 显性等待，判断元素是否可点击
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14",
  "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
  # "appium:noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

try:
    # 检查“Alert Views”元素是否可点击
    ele = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Alert Views')))
    ele.click()
except Exception as e:
    raise e
finally:
    sleep(2)
    driver.quit()
