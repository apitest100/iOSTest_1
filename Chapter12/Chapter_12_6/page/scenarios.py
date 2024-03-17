from Chapter12.Chapter_12_6.page.operations import *


class GoodsScenario(object):
    """
    这里定义商品相关的场景
    """
    # 场景一：搜索商品，进入详情页
    def search_goods(self, book_name, author, storm):
        HomePageOpn(storm).click_search_box()
        HomePageOpn(storm).search_goods(book_name)
        HomePageOpn(storm).click_search_btn()
        BookPageOpn(storm).click_jd()
        BookPageOpn(storm).click_list_author(author)

    # 场景二：搜索商品，加入购物车
    def add_cart(self, book_name, author, storm):
        HomePageOpn(storm).click_search_box()
        HomePageOpn(storm).search_goods(book_name)
        HomePageOpn(storm).click_search_btn()
        BookPageOpn(storm).click_jd()
        BookPageOpn(storm).click_list_author(author)
        BookPageOpn(storm).click_add2card_btn()
        try:
            BookPageOpn(storm).click_ok_btn()
            BookPageOpn(storm).click_close_icon()
        except Exception:
            pass

    # 场景三：搜索商品，收藏商品
    def collect_goods(self, book_name, author, storm):
        HomePageOpn(storm).click_search_box()
        HomePageOpn(storm).search_goods(book_name)
        HomePageOpn(storm).click_search_btn()
        BookPageOpn(storm).click_jd()
        BookPageOpn(storm).click_list_author(author)
        BookPageOpn(storm).click_collection_btn()

if __name__ == '__main__':
    GoodsScenario().search_goods('sss')