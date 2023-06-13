# coding:utf-8
# Name:test_element.py
# Author:nigo
# Time:2022/10/20 5:07 下午 
# Description:元素定位
# 以下课件
# xpath (xml path langage)解析html与xml；速度比css慢，从头到尾遍历；selenium和appium都可用
# 浏览器console $x('//*[@id="s_tab"]//a[last()-1]')，用xpth选取所有元素 id属性=s_tab 下面a标签倒数第二个
# css select (css样式)原生的appium不支持css，webview可以使用，通过样式查找速度比selenium快
# $('#kw') $('[id=kw]') id=kw; div,p 所有div元素和p元素; div p div元素内部的所有p元素(div的子孙);
# div>p 父元素为div的所有p元素（div的子）; p:nth-child(2) p的父元素的第2个孩子 p:nth-last-child(1);
# div+p 紧接div元素后的所有p元素; p~ul 前面有p元素的每个ul元素

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestElement():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def test_element(self):
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("bipo")
        self.driver.find_element(By.ID, 'su').click()
