# coding:utf-8
# Name:test_TouchAction.py
# Author:nigo
# Time:2022/10/21 6:30 下午 
# Description:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import TouchActions

class TestTouchAction():
    def setup(self):
        #
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        '''
        输入""
        通过TouchAction 点击搜索
        滑动到底部，点击下一页
        关闭Chrome
        :return:
        '''
        self.driver.get("http://www.baidu.com")
        el = self.driver.find_element(By.CSS_SELECTOR,"#kw")
        el_search = self.driver.find_element(By.CSS_SELECTOR,"#su")

        el.send_keys("selenium")
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()

        action.scroll_from_element(el,0 ,10000).perform()