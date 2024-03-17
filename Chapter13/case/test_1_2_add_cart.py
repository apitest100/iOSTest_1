import pytest
from Chapter13.common.parse_csv import parse_csv
from Chapter13.page.scenarios import *
import os

data_file = os.path.join(os.path.dirname(os.getcwd()),'data/test_1_2_add_cart.csv')


@pytest.mark.parametrize(("book_name", "author"), parse_csv(data_file))
class TestAddCart(object):
    """
    测试加入购物车功能，加购后，购物车有该物品
    """
    @pytest.mark.L1
    def test_add_cart(self, book_name, author, storm):
        # 点击首页搜索框
        GoodsScenario().add_cart(book_name, author, storm)
        # 点击"返回"按钮，返回到商品搜索列表页面
        BookPageOpn(storm).click_back_btn()
        BookPageOpn(storm).click_back_btn()
        BookPageOpn(storm).click_back_btn()
        # 点击"购物车"
        ShopCartPageOpn(storm).click_shopcart_label()
        # 将第一本书的书名存储到变量book_name1
        book_name1 = ShopCartPageOpn(storm).get_book_name_first()
        print('the book name is {}'.format(book_name1))
        # 断言目标书籍加购成功
        assert book_name in book_name1


if __name__ == '__main__':
    pytest.main(["-s"])