# coding:utf-8
# Name:test.performance.py
# Author:nigo
# Time:2021/4/25 9:00 下午 
# Description:
from selenium import webdriver
class TestData:
    def test_data(self):
        driver = webdriver.Chrome()
        driver.get("www.google.com")
        print(driver.execute_script("return JSON.stringify(window.performance.timing)"))
