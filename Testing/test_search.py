# encoding=utf-8
import pytest
from appium import webdriver


class TestXueQiu:
    def setup(self):
        print("setup")
        capabilities = {
            "platformName": "Android",
            "deviceName": "CUYDU19524012040",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias"
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
        self.driver.implicitly_wait(10)

    def teardown(self):
        print("teardown")
        self.driver.quit()

    def test_search(self):
        print("search")
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        el1.click()
        # el2 = self.driver.find_element_by_id("com.xueqiu.android:id/image_cancel")
        # el2.click()
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                "/android.widget.FrameLayout/android.view.ViewGroup/android.widget"
                                                ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                                "/android.widget.FrameLayout/android.widget.RelativeLayout/android"
                                                ".view.ViewGroup/android.widget.LinearLayout/android.widget"
                                                ".RelativeLayout["
                                                "1]/android.widget.RelativeLayout/android.widget.ViewFlipper/android"
                                                ".widget.LinearLayout/android.widget.TextView")
        el3.send_keys("alibaba")


if __name__ == '__main__':
    pytest.main()
