from appium import webdriver
from time import sleep
import pytest
from Chapter13.common.parse_yaml import parse_yaml
import os


# 全局设置driver方法1
driver = None
data_file = os.path.join(os.path.dirname(os.getcwd()),'config/desired_caps.yaml')

# scope="module"，每个Python文件执行一次启动和结束driver
@pytest.fixture(scope="function")
def storm():
    global driver
    caps = parse_yaml(data_file, 'jd_caps')
    remote = parse_yaml(data_file, 'jd_remote', 'remote')
    driver = webdriver.Remote(remote, caps)
    driver.implicitly_wait(10)
    yield driver
    # 休眠1秒，然后退出driver
    sleep(1)
    driver.quit()
