import pytest
import sys


class Test01(object):
    """
    sys.platform可以获取当前操作系统信息：
    Windows系统：win32
    linux系统：linux2
    Mac系统：darwin
    """
    @pytest.mark.skipif(sys.platform == 'darwin', reason='不在Mac OS执行')
    def test_01(self):
        print('---用例01---')

    def test_02(self):
        print('---用例02---')

    def test_03(self):
        print('---用例03---')