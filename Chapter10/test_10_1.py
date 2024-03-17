import pytest


class TestStorm(object):
    def test_a(self):
        print('This is a')
        assert 'a' == 'a'

    def test_b(self):
        print('This is b')
        assert 'b' == 'c'


