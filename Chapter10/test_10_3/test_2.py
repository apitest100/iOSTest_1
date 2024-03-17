import pytest, allure

@allure.feature("测试场景2")      #标记场景
class TestDemo():
    @allure.story("测试用例2-1")   #标记用例
    @allure.severity("minor")    #标记用例级别
    def test_2_1(self):
        """
        用例描述：这是测试用例2-1的用例描述
        """
        # allure.MASTER_HELPER.description("11111111111111")
        a = 1 + 1
        assert a == 3  # 断言失败

    @allure.story("测试用例2-2")
    @allure.severity("minor")
    @allure.step('用例2:重要步骤')
    def test_2_2(self):
        """
        用例描述：这是测试用例2-2的用例描述
        """
        assert 2 == 2