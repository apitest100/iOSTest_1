import pytest


class TestTwo(object):
    def test_2_1(self, sutd):
        print("test2_1")

    def test_2_2(self, sutd):
        print("test2_2")

    def test_2_3(self, sutd):
        print("test2_3")


if __name__ == '__main__':
    pytest.main()
