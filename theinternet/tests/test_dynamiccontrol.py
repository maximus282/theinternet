import time

import pytest
from selenium import webdriver

import unittest
from theinternet.pages.dynamiccontrol_page import DynamicControlPage

from theinternet.config.config import base_url
from theinternet.tests.basetest import BaseTest


class TestDynContrPage(BaseTest):

    def test_checkbox_check(self):
        print("Test started: checkbox")
        dyn_contr_page=DynamicControlPage(self.driver)

        self.driver.get(base_url + "dynamic_controls")
        assert dyn_contr_page.checkbox_select_status() == False
        dyn_contr_page.click_checkbox()
        time.sleep(2)
        assert dyn_contr_page.checkbox_select_status() == True

    def test_checkbox_check_uncheck(self):
        print("Test started: checkbox")
        dyn_contr_page=DynamicControlPage(self.driver)

        self.driver.get(base_url + "dynamic_controls")
        assert dyn_contr_page.checkbox_select_status() == False
        dyn_contr_page.click_checkbox()
        time.sleep(2)
        assert dyn_contr_page.checkbox_select_status() == True
        dyn_contr_page.click_checkbox()
        time.sleep(2)
        assert dyn_contr_page.checkbox_select_status() == False


    def test_checkbox_remove(self):
        print("Test started: checkbox")
        dyn_contr_page=DynamicControlPage(self.driver)

        self.driver.get(base_url + "dynamic_controls")
        assert dyn_contr_page.checkbox_display_status() == True
        dyn_contr_page.click_remove_btn()
        time.sleep(3)
        assert dyn_contr_page.assert_checkbox_dissappeared() == True

    def test_checkbox_remove_add(self):
        print("Test started: checkbox")
        dyn_contr_page=DynamicControlPage(self.driver)

        self.driver.get(base_url + "dynamic_controls")
        assert dyn_contr_page.checkbox_display_status() == True
        dyn_contr_page.click_remove_btn()
        assert dyn_contr_page.assert_checkbox_dissappeared() == True
        dyn_contr_page.click_add_btn()
        assert dyn_contr_page.assert_checkbox_appeared() == True


