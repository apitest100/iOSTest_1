from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import pytest


data = [['Python实现Web UI自动化测试实战', 'Storm,李鲲程,边宇明', 'Storm'], ]


@pytest.mark.parametrize(("book_name", "author", "target"), data)
class TestHomeSearch(object):
    """
    测试首页的搜索功能
    """
    def setup(self):
        # 初始化driver
        caps = {
            "appium:platformName": "iOS",
            "appium:platformVersion": "16.3.1",
            "appium:deviceName": "iPhone 12",
            "appium:udid": "00008101-000B64AE3C98001E",
            "appium:bundleId": "com.360buy.jdmobile",
            # "appium:noReset": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        print(self.driver.orientation)

    def teardown(self):
        # 休眠1秒，然后退出driver
        sleep(1)
        self.driver.quit()

    @pytest.mark.L1
    def test_search(self, book_name, author, target):
        # 点击首页搜索框
        self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name CONTAINS "搜索栏"').click()
        # 在新打开的搜索页面，搜索框中输入“Web UI自动化测试”，点击”搜索“
        # 注意新打开页面的搜索框
        self.driver.find_element(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeSearchField"').send_keys(
            book_name)
        # 点击搜索按钮
        self.driver.find_element(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" and name == "搜索"').click()
        # 点击京东物流，筛选京东物流的书籍
        self.driver.find_element(AppiumBy.IOS_PREDICATE, 'label == "京东物流" AND name == "京东物流"').click()
        # 点击第一本"Python实现Web UI自动化测试实战"这本书，进入商品详情页
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, author).click()
        # 找到作者元素
        ele = self.driver.find_element(AppiumBy.IOS_PREDICATE, 'label == "{}"'.format(author))
        # 将作者信息保存到ele_txt中
        ele_txt = ele.text
        print('作者信息：{}'.format(ele_txt))
        # 断言'Storm'是作者之一
        assert target in ele_txt


if __name__ == '__main__':
    pytest.main(["-s"])
