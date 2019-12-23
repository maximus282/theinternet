import random
import time

import pytest
from selenium import webdriver

import unittest
from theinternet.pages.alert_page import AlertPage

from theinternet.config.config import base_url
from theinternet.tests.basetest import BaseTest


def get_url():
    print("My fixture")
    return base_url+"javascript_alerts"


class TestAlertPage(BaseTest):

    #test_data
    data=[("mytext1"),(" "),(123)]

    def test_jsalert_accept(self):
        print("Test started: JS alerts")
        alert_page=AlertPage(self.driver)

        self.driver.get(base_url+"javascript_alerts")
        alert_page.click_alert_btn()
        alert_page.accept_popup()
        assert "You successfuly clicked an alert" == alert_page.display_return_msg()

    def test_jsconfirm_accept(self):
        print("Test started: JS confirmations")
        alert_page = AlertPage(self.driver)

        self.driver.get(base_url + "javascript_alerts")
        alert_page.click_conf_btn()
        alert_page.accept_popup()
        assert "You clicked: Ok" == alert_page.display_return_msg()

    def test_jsconfirm_dismiss(self):
        print("Test started: JS confirmations")
        alert_page = AlertPage(self.driver)

        self.driver.get(base_url + "javascript_alerts")
        alert_page.click_conf_btn()
        alert_page.dismiss_popup()
        assert "You clicked: Cancel" == alert_page.display_return_msg()

    @pytest.mark.parametrize("data_input", data)
    def test_jsprompt_accept(self,data_input):
        print("Test started: JS confirmations")
        alert_page = AlertPage(self.driver)

        self.driver.get(base_url + "javascript_alerts")
        alert_page.click_prompt_btn()
        alert_page.sendkeys_popup(data_input)
        alert_page.accept_popup()
        assert alert_page.display_return_msg() == ("You entered: " + str(data_input)).rstrip()
        time.sleep(3)


    @pytest.mark.parametrize("data_input", data)
    def test_jsprompt_dismiss(self, data_input):
        print("Test started: JS confirmations")
        alert_page = AlertPage(self.driver)

        self.driver.get(base_url + "javascript_alerts")
        alert_page.click_prompt_btn()
        alert_page.sendkeys_popup(data_input)
        # time.sleep(2)
        alert_page.dismiss_popup()
        assert alert_page.display_return_msg() == "You entered: null"


