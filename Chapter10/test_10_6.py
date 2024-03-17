import pytest

'''
在class中不要同时使用“setup_method/teardown_method”和“setup/teardown”，否则“setup/teardown”不生效
'''
class Test01(object):
    def setup_class(self):
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')

    def setup_method(self):
        print('setup_method')

    def teardown_method(self):
        print('teardown_method')

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

