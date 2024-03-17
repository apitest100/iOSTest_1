from appium import webdriver
from time import sleep


# 定义一个字典
caps = {}
# 平台名
caps["appium:platformName"] = "iOS"
# 平台版本
caps["appium:platformVersion"] = "16.2"
# 设备名
caps["appium:deviceName"] = "iPhone 14"
# App路径
caps["appium:app"] = "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app"
# 是否重置App
caps["appium:noReset"] = True
# 初始化driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
# 休眠3秒
sleep(3)
driver.quit()
