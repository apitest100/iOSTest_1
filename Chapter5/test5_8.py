from appium import webdriver
from time import sleep


# 激活App
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14",
}
# 因为Caps中未指定app参数，因此不会安装和启动任何App
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
# activate_app('bundle_id')，激活App
driver.activate_app('com.storm.apple-samplecode.UICatalog')
sleep(3)
driver.quit()
