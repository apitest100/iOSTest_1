from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import pytest
from Chapter12.Chapter_12_1.parse_yaml import parse_yaml


data = [['Python实现Web UI自动化测试实战', 'Storm,李鲲程,边宇明', 'Storm'], ]


@pytest.mark.parametrize(("book_name", "author", "target"), data)
class TestPay(object):
    """
    测试结算商品功能，判断"提交订单"按钮可点击
    """
    def setup(self):
        caps = parse_yaml('desired_caps.yaml', 'jd_caps')
        remote = parse_yaml('desired_caps.yaml', 'jd_remote', 'remote')
        self.driver = webdriver.Remote(remote, caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # 休眠1秒
        sleep(1)
        self.driver.quit()

    @pytest.mark.L1
    def test_pay(self, book_name, author, target):
        # 点击首页搜索框
        self.driver.find_element(AppiumBy.IOS_PREDICATE, 'name CONTAINS "搜索栏"').click()
        # 在新打开的搜索页面，搜索框中输入“Web UI自动化测试”，点击”搜索“
        # 注意新打开页面的搜索框
        self.driver.find_element(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeSearchField"').send_keys(
            book_name)
        # 点击搜索按钮
        self.driver.find_element(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" and name == "搜索"').click()
        # 点击京东物流，筛选京东物流的书籍
        self.driver.find_element(AppiumBy.IOS_PREDICATE,
                                 'label == "京东物流" AND name == "京东物流" AND value == "京东物流"').click()
        # 点击第一本"Python实现Web UI自动化测试实战"这本书，进入商品详情页
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, author).click()
        # 单击加入购物车按钮
        self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                 '**/XCUIElementTypeStaticText[`label == "加入购物车"`]').click()
        # 点击"返回"按钮，返回到商品搜索列表页面
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '返回').click()
        # 再次点击"返回"按钮，返回到搜索页面
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '返回').click()
        # 点击"返回"按钮，返回到首页页面
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '返回').click()
        # 点击购物车,第4个标签
        self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "购物车"`]').click()
        # 点击去结算,这个地方不能直接用Inspector提供的定位器，不同书籍数量，文字不同
        self.driver.find_element(AppiumBy.IOS_PREDICATE, 'label CONTAINS "去结算"').click()
        # 断言：进入到"确认订单"页面，该页面"提交订单"按钮可点击，属性为enabled
        ele = self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "提交订单"`]')
        assert 'true' == ele.get_attribute('enabled')


if __name__ == '__main__':
    pytest.main(["-s"])