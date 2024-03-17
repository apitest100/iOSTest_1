import pytest


class Test01(object):
    @pytest.mark.skipif(2>1, reason='2>1为真，不执行')
    def test_a(self):
        print('aaaa')
        assert 'a' == 'a'

    def test_b(self):
        print('bbbb')
        assert 'b' == 'b'