import pytest
from Chapter12.Chapter_12_6.parse_csv import parse_csv
from Chapter12.Chapter_12_6.page.scenarios import *

data = parse_csv('../test_1_1_home_search.csv')


@pytest.mark.parametrize(("book_name", "author", "target", "publisher"), data)
class TestHomeSearch(object):
    """
    测试首页的搜索功能
    """
    @pytest.mark.L1
    def test_search(self, book_name, author, target, publisher, storm):
        GoodsScenario().search_goods(book_name, author, storm)
        # 向上滑动屏幕
        storm.execute_script('mobile: swipe', {'direction': 'up'})
        # 将作者信息保存到ele_txt中
        ele_txt = BookPageOpn(storm).get_detail_author(author)
        print('作者信息：{}'.format(ele_txt))
        # 断言一：作者
        assert target in ele_txt
        # 断言二：出版社
        publisher_1 = BookPageOpn(storm).get_detail_publish(publisher)
        print('出版社信息：{}'.format(publisher_1))
        assert publisher_1 in publisher


if __name__ == '__main__':
    pytest.main(["-s"])