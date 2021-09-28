# encoding=utf-8
#查找，点击等基本方法
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver
    def __init__(self,driver:WebDriver = None):
        self._driver = driver

    def find(self,locator,value):
        return self._driver.find_element(locator,value)





