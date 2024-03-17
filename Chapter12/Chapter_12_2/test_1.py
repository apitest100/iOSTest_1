import pytest


class TestOne(object):
    def test_1_1(self, sutd):
        print('test1_1')

    def test_1_2(self, sutd):
        print('test1_2')

    def test_1_3(self, sutd):
        print('test1_3')



if __name__ == '__main__':
    pytest.main()
