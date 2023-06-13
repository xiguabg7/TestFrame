# coding:utf-8
# Name:test_wait.py
# Author:nigo
# Time:2022/10/20 3:42 下午 
# Description:三种等待，直接等待，显示等待，隐式等待
from time import sleep
from selenium import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://global-test-butter.bipocloud.com/")
        # 全局find 隐式等待3秒（轮询查找（默认0.5秒）元素是否出现,如果没出现就抛异常）
        self.driver.implicitly_wait(3)

    def test_wait(self):
        # 直接等待
        # sleep(5)

        # 通过条件判断，执行显示等待，自定义wait函数,注意函数传参
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@title="XXXXXX"]')) > 1
        # 显式等待,until()括号中将method当作参数传入,method不要加(),否则是调用函数
        WebDriverWait(self.driver, 10).until(wait)

        # selenium自带的条件判断
        WebDriverWait(self.driver, 10).until(expected_conditions.element_located_to_be_selected(By.XPATH, '//*[@title="XXXXXX"]'))

# if __name__=="__main__":
#     pytest.main(['test_wait.py'])
