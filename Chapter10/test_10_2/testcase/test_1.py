import pytest

class TestStorm1(object):
    @pytest.mark.L1
    def test_01(self):
        print('aaa')
        assert 'a'=='a'


