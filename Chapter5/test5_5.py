from appium import webdriver
from time import sleep


# 判断App是否安装
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14",
  "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",

}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
# 这里需要传递bundle_id
res = driver.is_app_installed("com.storm.apple-samplecode.UICatalog")
print(res)
# 休眠3秒
sleep(3)
driver.quit()
