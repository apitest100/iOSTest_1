from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import pytest
from Chapter12.Chapter_12_1.parse_yaml import parse_yaml


data = [['Python实现Web UI自动化测试实战', 'Storm,李鲲程,边宇明', 'Storm'], ]


@pytest.mark.parametrize(("book_name", "author", "target"), data)
class TestAddCart(object):
    """
    测试收藏功能
    """
    def setup(self):
        caps = parse_yaml('desired_caps.yaml', 'jd_caps')
        remote = parse_yaml('desired_caps.yaml', 'jd_remote', 'remote')
        self.driver = webdriver.Remote(remote, caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.L2
    def test_add_cart(self,book_name,author,target):
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
        # 单击加入收藏按钮
        self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "收藏"`][2]').click()
        # 点击"返回"按钮，返回到商品搜索列表页面
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '返回').click()
        # 再次点击"返回"按钮，返回到搜索页面
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '返回').click()
        # 点击"返回"按钮，返回到首页页面
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '返回').click()

        # 点击"我的"
        self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "我的"`]').click()
        # 点击商品收藏，进入收藏详情列表
        self.driver.find_element(AppiumBy.IOS_PREDICATE, 'label == "商品收藏"').click()
        # 将书籍名包含"Web UI自动化测试"的书籍名放入变量bookname中
        book_name1 = self.driver.find_element(AppiumBy.IOS_PREDICATE,
                                              'label CONTAINS "{}"'.format(book_name)).get_attribute('name')
        print('the book name is {}'.format(book_name1))
        # 断言：加入收藏的书籍在书籍列表可见
        assert book_name in book_name1
        # 将商品取消收藏
        # 左滑商品
        # self.driver.execute_script('mobile: swipe', {'direction': 'right'})
        book_ele = self.driver.find_element(AppiumBy.IOS_PREDICATE,
                                            'label CONTAINS "{}"'.format(book_name))
        self.driver.execute_script('mobile: swipe', {'direction': 'left', 'element': book_ele, "duration": 1})
        # 点击取消收藏
        self.driver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                 '**/XCUIElementTypeButton[`label == "取消 收藏"`][1]').click()


if __name__ == '__main__':
    pytest.main(["-s"])