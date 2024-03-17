import pytest

'''
在class中使用：
1、setup_class、teardown_class，在整个class的开始和最后运行一次；
2、setup和teardown，在每个方法（类中的函数叫方法）开始前后执行；
'''
class Test01(object):
    def setup_class(self):
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')


    def test_a(self):
        print('aaaa')
        assert 'a' == 'a'

    def test_b(self):
        print('bbbb')
        assert 'b' == 'b'

