# coding:utf-8
# Name:web_driver.py
# Author:nigo
# Time:2022/10/19 6:39 下午 
# Description:

from selenium import webdriver

# 调用webdriver
driver = webdriver.Chrome()  # executable_path="/usr/local/bin/chromedriver"
driver.get("https://www.baidu.com")
# 最大化窗口
driver.maximize_window()
# 全局隐式等待5秒（轮询查找（默认0.5秒）元素是否出现,如果没出现就抛异常）
driver.implicitly_wait(5)
# 退出
driver.quit()

# class TestWeb():
#
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(5)
#
#     def teardown(self):
#         # pass
#         self.driver.quit()
#
#     def test_web(self):
#         self.driver.get("https://www.baidu.com")
