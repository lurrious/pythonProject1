# encoding=utf-8
# app的首页
import pytest

from Testing.test.PageObject.base_page import BasePage


class Main(BasePage):
    @pytest.fixture()
    def find(self, locator, value):
        return self._driver.find_element(locator, value)
