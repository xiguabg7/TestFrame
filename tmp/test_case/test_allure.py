import pytest
import yaml
#
#
# class Data:
#
#     @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./data.yaml")))
#     def test_add(self, a, b):
#         print(a + b)
#
#     def test_yaml(self):
#         print(yaml.safe_load(open("./date.yml")))
import allure


@allure.feature("login模块")
class TestLogin():
    @allure.story("登陆成功")
    def test_login_one(self):
        with allure.step("pass"):
            print("one")

    @allure.story("登陆失败")
    def test_login_two(self):
        with allure.step("fail"):
            print("one")

    @allure.story("密码确实")
    def test_login_three(self):
        with allure.step("大小写不符"):
            print("one")
        with allure.step("..."):
            print("two")
        pass

# 执行.py文件的结果，生产json，保存起来
# pytest test_allure.py --alluredir=./tmpt
# #结果在allure中展示
# allure serve ./tmpt
# 打开报告
# allure open 报告目录/
