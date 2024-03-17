from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import pytest


data = ['storm', 123, '中文', '!@#']

@pytest.mark.parametrize("s_txt", data)
class TestTextFields():
    def setup(self):
        caps = {
            "appium:platformName": "iOS",
            "appium:platformVersion": "16.4",
            "appium:deviceName": "iPhone 14",
            "appium:app": "/Users/juandu/Library/Developer/Xcode/DerivedData/UIKitCatalog-gdzebhtrarkehxetojfioimyqtls/Build/Products/Debug-iphonesimulator/UIKitCatalog.app",
            # "appium:noReset": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def teardown(self):
        # 休眠1秒
        sleep(1)
        self.driver.quit()

    def test_send_1(self, s_txt):
        # 定位元素Text Fields，并点击
        ele1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Text Fields')
        ele1.click()
        # 这里不推荐使用-ios class chain
        # 定位文本框，输入文字"Storm"
        ele2 = self.driver.find_elements(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextField"')
        ele2[0].send_keys(s_txt)
        # 如果s_txt是数字，要先转换成同类型再比较
        if type(s_txt) == int:
            assert ele2[0].text == str(s_txt)
        else:
            assert ele2[0].text == s_txt


if __name__ == '__main__':
    pytest.main(["-s"])
