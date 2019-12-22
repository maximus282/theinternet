import time

import pytest
from selenium import webdriver

import unittest
from theinternet.pages.dynamiccontrol import DynamicControlPage

baseURL="https://the-internet.herokuapp.com/"

@pytest.mark.usefixtures("setup")
class LoginTest(unittest.TestCase):

    def test_checkbox_enable(self):
        print("Test started: get geolocation")
        dyn_contr_page=DynamicControlPage(self.driver)

        self.driver.get(baseURL + "dynamic_controls")
        assert dyn_contr_page.checkbox_select_status() == False
        dyn_contr_page.click_checkbox()
        time.sleep(2)
        assert dyn_contr_page.checkbox_select_status() == True


    def test_checkbox_remove(self):
        print("Test started: get geolocation")
        dyn_contr_page=DynamicControlPage(self.driver)

        self.driver.get(baseURL + "dynamic_controls")
        assert dyn_contr_page.checkbox_display_status() == True
        dyn1=dyn_contr_page.click_remove_btn()
        # time.sleep(2)
        assert dyn1.checkbox_display_status() == True