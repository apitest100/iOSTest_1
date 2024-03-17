import pytest,allure

@allure.feature("测试场景1")      #标记场景
class TestDemo():
    @allure.story("测试用例1-1") # 标记测试用例
    @allure.severity("trivial") # 标记用例级别
    @allure.step('测试步骤1：准备活动')
    def test_1_1(self): # 用例1
        """
        用例描述：这是测试用例1-1的用例描述
        """
        assert 2 == 2

    @allure.story("测试用例1-2")
    @allure.severity("critical")
    def test_1_2(self):
        """
        用例描述：这是测试用例1-2的用例描述
        """
        assert 2 == 2
