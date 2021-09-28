# encoding=utf-8
# 启动动作
from appium import webdriver

from Testing.test.PageObject.base_page import BasePage


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActoivityAlias"

    def start(self):
        caps = {
            "platformName": "Android",
            "deviceName": "CUYDU19524012040",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True
        }
        self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self._driver.implicitly_wait(3)
        return self

    def main(self) -> Main:
        return Main()
