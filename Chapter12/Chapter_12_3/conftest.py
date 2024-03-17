from appium import webdriver
from time import sleep
import pytest
from Chapter12.Chapter_12_3.parse_yaml import parse_yaml

# 全局设置driver方法1
driver = None

# scope="function"，每个函数或方法执行一次启动和结束driver
@pytest.fixture(scope="function")
def storm():
    global driver
    caps = parse_yaml('desired_caps.yaml', 'jd_caps')
    remote = parse_yaml('desired_caps.yaml', 'jd_remote', 'remote')
    driver = webdriver.Remote(remote, caps)
    driver.implicitly_wait(10)
    yield driver
    # 休眠1秒，然后退出driver
    sleep(1)
    driver.quit()
