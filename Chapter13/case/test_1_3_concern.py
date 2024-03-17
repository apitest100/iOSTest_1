import pytest
from Chapter13.common.parse_csv import parse_csv
from Chapter13.page.scenarios import *
import os


data_file = os.path.join(os.path.dirname(os.getcwd()),'data/test_1_2_add_cart.csv')


@pytest.mark.parametrize(("book_name", "author"), parse_csv(data_file))
class TestAddCart(object):
    """
    测试收藏功能
    """
    @pytest.mark.L2
    def test_add_cart(self, book_name, author, storm):
        # 点击首页搜索框
        GoodsScenario().collect_goods(book_name, author, storm)
        # 点击"返回"按钮，返回到商品搜索列表页面
        BookPageOpn(storm).click_back_btn()
        BookPageOpn(storm).click_back_btn()
        BookPageOpn(storm).click_back_btn()
        # 点击"我的"
        PersonPageOpn(storm).click_person_label()
        # 点击商品收藏，进入收藏详情列表
        PersonPageOpn(storm).click_product_collection()
        # 将书籍名包含"Web UI自动化测试"的书籍名放入变量bookname中
        book_name1 = CollectionPageOpn(storm).get_collect_goods_first(book_name).get_attribute('name')
        print('the book name is {}'.format(book_name1))
        # 断言：加入收藏的书籍在书籍列表可见
        assert book_name in book_name1
        # 将商品取消收藏
        # 左滑商品
        book_ele = CollectionPageOpn(storm).get_collect_goods_first(book_name)
        storm.execute_script('mobile: swipe', {'direction': 'left', 'element': book_ele, "duration": 1})
        # 点击取消收藏
        CollectionPageOpn(storm).click_uncollect()


if __name__ == '__main__':
    pytest.main(["-s"])