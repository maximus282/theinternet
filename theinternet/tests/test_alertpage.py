import random
import time

import pytest
from selenium import webdriver

import unittest
from theinternet.pages.alert import AlertPage

baseURL="https://the-internet.herokuapp.com/"

@pytest.mark.usefixtures("setup")
class LoginTest(unittest.TestCase):


    def test_jsalert_accept(self):
        print("Test started: JS alerts")
        alert_page=AlertPage(self.driver)

        self.driver.get(baseURL + "javascript_alerts")
        alert_page.click_alert_btn()
        alert_page.accept_popup()
        assert "You successfuly clicked an alert" == alert_page.display_return_msg()

    def test_jsconfirm_accept(self):
        print("Test started: JS confirmations")
        alert_page = AlertPage(self.driver)

        self.driver.get(baseURL + "javascript_alerts")
        alert_page.click_conf_btn()
        alert_page.accept_popup()
        assert "You clicked: Ok" == alert_page.display_return_msg()

    def test_jsconfirm_dismiss(self):
        print("Test started: JS confirmations")
        alert_page = AlertPage(self.driver)

        self.driver.get(baseURL + "javascript_alerts")
        alert_page.click_conf_btn()
        alert_page.dismiss_popup()
        assert "You clicked: Cancel" == alert_page.display_return_msg()


    def test_jsprompt_accept(self):
        print("Test started: JS confirmations")
        alert_page = AlertPage(self.driver)
        # my_text="Random Text"+str(random.randint(0,1000))
        my_text=123

        self.driver.get(baseURL + "javascript_alerts")
        alert_page.click_prompt_btn()
        alert_page.sendkeys_popup(my_text)
        # time.sleep(2)
        alert_page.accept_popup()
        assert alert_page.display_return_msg() == "You entered: " + str(my_text)

    @pytest.mark.parametrize('name', ['Claire', 'Gloria', 'Haley'])
    def test_jsprompt_dismiss(self,name):
        print("Test started: JS confirmations")
        alert_page = AlertPage(self.driver)

        self.driver.get(baseURL + "javascript_alerts")
        alert_page.click_prompt_btn()
        alert_page.sendkeys_popup(name)
        # time.sleep(2)
        alert_page.dismiss_popup()
        assert alert_page.display_return_msg() == "You entered: null"


