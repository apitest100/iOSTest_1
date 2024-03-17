from appium import webdriver
from time import sleep


# 移除指定App
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
# remove_app('bundle_id')，移除App
driver.remove_app('com.storm.apple-samplecode.UICatalog')
sleep(3)
driver.quit()
