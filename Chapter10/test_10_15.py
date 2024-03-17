import pytest


class Test01(object):

    @pytest.mark.xfail()
    def test_01(self):
        print('---用例01---,该功能暂未实现！')

    def test_02(self):
        print('---用例02---')

    @pytest.mark.xfail()
    def test_03(self):
        print('---用例03---,预期用例失败！')
        assert 1 == 2