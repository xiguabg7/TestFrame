import allure


@allure.link("http://www.baidu.com", name="链接")
def test_with_link():
    print("link测试")
    pass


test_case_link = "http://www.baidu.com"
@allure.testcase(test_case_link, "登陆用例")
def test_with_testcase_link():
    print("testcase链接")
    pass

# --allure-link-pattern=issue:http://www.baidu.com/issue/{}
# --allure-link-pattern=issue:https://www.tapd.cn/35581150/search/get?keyword={}
# 以上链接是bug地址
# pytest test_allure_link.py --allure-link-pattern=issue:http://ww.baidu.com/issue/{} --alluredir=./res/3
# allure serve ./res/3
@allure.issue("1135581150001005663", "bug")
def test_with_issue_link():
    print("issue链接")
    pass
