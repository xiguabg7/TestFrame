# coding:utf-8
# Name:test_ActionChains.py
# Author:nigo
# Time:2022/10/20 11:21 下午 
# Description:web交互控件
# 执行原理：调用ActionChains(PC端操作)方法时，不会立即执行，而是将所有操作按顺序放在队列里，调用 perform()方法时，依次执行
# 基本用法：
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, r"//input[@value='click me']")
        element_doubleclick = self.driver.find_element(By.XPATH, r"//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element(By.XPATH, r"//input[@value='right click me']")
        action = ActionChains(self.driver)
        # 左键点击
        action.click(element_click)
        # 右键点击
        action.context_click(element_rightclick)
        # 双击
        action.double_click(element_doubleclick)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element(By.CSS_SELECTOR, "[id=s-usersetting-top]")
        action = ActionChains(self.driver)
        # 移动光标
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        drag_ele = self.driver.find_element(By.CSS_SELECTOR, "#dragger")
        drop_ele = self.driver.find_element(By.XPATH, "/html/body/div[2]")
        action = ActionChains(self.driver)
        # 从源位置拖拽到指定位置并释放
        # action.drag_and_drop(drag_ele,drop_ele).perform()
        # action.click_and_hold(drag_ele).release(drop_ele).perform()
        action.click_and_hold(drag_ele).move_to_element(drop_ele).release().perform()
        sleep(3)

    @pytest.mark.skip
    def test_keys(self):
        self.driver.get("https://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(By.XPATH, "/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        # Keys键盘按键
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)


