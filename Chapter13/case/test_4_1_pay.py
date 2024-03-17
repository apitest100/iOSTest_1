import pytest
from Chapter13.common.parse_csv import parse_csv
from Chapter13.page.scenarios import *
import os


data_file = os.path.join(os.path.dirname(os.getcwd()),'data/test_1_2_add_cart.csv')


@pytest.mark.parametrize(("book_name", "author"), parse_csv(data_file))
class TestPay(object):
    """
    测试结算商品功能，判断"提交订单"按钮可点击
    """
    @pytest.mark.L1
    def test_pay(self, book_name, author, storm):
        GoodsScenario().add_cart(book_name, author, storm)
        BookPageOpn(storm).click_back_btn()
        BookPageOpn(storm).click_back_btn()
        BookPageOpn(storm).click_back_btn()
        # 点击购物车,第4个标签
        ShopCartPageOpn(storm).click_shopcart_label()
        # 点击去结算,这个地方不能直接用Inspector提供的定位器，不同书籍数量，文字不同
        ShopCartPageOpn(storm).click_settlement_btn()
        # 断言：进入到"确认订单"页面，该页面"提交订单"按钮可点击，属性为enabled
        attr = ShopCartPageOpn(storm).get_submit_btn_status()
        assert 'true' == attr


if __name__ == '__main__':
    pytest.main(["-s"])