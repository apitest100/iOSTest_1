import pytest


class Test01(object):
    @pytest.mark.skip(reason='这里标记原因')
    def test_a(self):
        print('aaaa')
        assert 'a' == 'a'

    def test_b(self):
        print('bbbb')
        assert 'b' == 'b'