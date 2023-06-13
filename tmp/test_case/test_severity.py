import allure


# 阻塞
@allure.severity(allure.severity_level.BLOCKER)
def test_with_severity1():
    pass


# 严重
@allure.severity(allure.severity_level.CRITICAL)
def test_with_severity2():
    pass


# 正常
@allure.severity(allure.severity_level.NORMAL)
def test_with_severity3():
    pass


# 不太重要
@allure.severity(allure.severity_level.MINOR)
def test_with_severity4():
    pass


# 不重要
@allure.severity(allure.severity_level.TRIVIAL)
def test_with_severity5():
    pass

#pytest test_severity.py --alluredir=./res/3 --allure-severities normal,critical
#allure serve ./res/3
