from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import pytest


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

    def test_send_1(self):
        # 定位元素Text Fields，并点击
        ele1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Text Fields')
        ele1.click()
        # 这里不推荐使用-ios class chain
        # 定位文本框，输入文字"Storm"
        ele2 = self.driver.find_elements(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextField"')
        ele2[0].send_keys('Storm')
        # print(ele2[0].text)
        assert ele2[0].text == 'Storm'


if __name__ == '__main__':
    pytest.main(["-s"])
