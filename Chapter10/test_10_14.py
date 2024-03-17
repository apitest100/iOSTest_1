import pytest


data = ['admin', 'storm']


def test_01():
    for name in data:
        if name == 'storm':
            pytest.skip('storm没有访问权限')
        else:
            print('{}有访问权限'.format(name))

