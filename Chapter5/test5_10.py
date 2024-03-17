from appium import webdriver
from time import sleep


# 获取App状态信息
caps = {
  "appium:platformName": "iOS",
  "appium:platformVersion": "16.2",
  "appium:deviceName": "iPhone 14",
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
# 等待3秒
sleep(3)
# desired_caps中没有App信息，因此不会启动,state=1
state0 = driver.query_app_state('com.storm.apple-samplecode.UICatalog')
print(state0)
# 激活UIKitCatalog App
driver.activate_app('com.storm.apple-samplecode.UICatalog')
sleep(3)
# 启动状态的App，App_state=4
state1 = driver.query_app_state('com.storm.apple-samplecode.UICatalog')
print(state1)
driver.terminate_app('com.storm.apple-samplecode.UICatalog')
sleep(2)
# 关闭状态的App，App_state=1
state2 = driver.query_app_state('com.storm.apple-samplecode.UICatalog')
print(state2)
driver.quit()
