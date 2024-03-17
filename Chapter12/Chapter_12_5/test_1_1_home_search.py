from appium.webdriver.common.appiumby import AppiumBy
import pytest
from Chapter12.Chapter_12_5.parse_csv import parse_csv

data = parse_csv('test_1_1_home_search.csv')


@pytest.mark.parametrize(("book_name", "author", "target"), data)
class TestHomeSearch(object):
    """
    测试首页的搜索功能
    """
    @pytest.mark.L1
    def test_search(self, book_name, author, target, storm):
        # 点击首页搜索框
        storm.find_element(AppiumBy.IOS_PREDICATE, 'name CONTAINS "搜索栏"').click()
        # 在新打开的搜索页面，搜索框中输入“Web UI自动化测试”，点击”搜索“
        # 注意新打开页面的搜索框
        storm.find_element(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeSearchField"').send_keys(
            book_name)
        # 点击搜索按钮
        storm.find_element(AppiumBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" and name == "搜索"').click()
        # 点击京东物流，筛选京东物流的书籍
        storm.find_element(AppiumBy.IOS_PREDICATE, 'label == "京东物流" AND name == "京东物流"').click()
        # 点击第一本"Python实现Web UI自动化测试实战"这本书，进入商品详情页
        storm.find_element(AppiumBy.ACCESSIBILITY_ID, author).click()
        # 找到作者元素
        ele = storm.find_element(AppiumBy.IOS_PREDICATE, 'label == "{}"'.format(author))
        # 将作者信息保存到ele_txt中
        ele_txt = ele.text
        print('作者信息：{}'.format(ele_txt))
        # 断言'Storm'是作者之一
        assert target in ele_txt


if __name__ == '__main__':
    pytest.main(["-s"])