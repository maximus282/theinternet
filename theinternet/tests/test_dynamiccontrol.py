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
        assert dyn_contr_page.checkbox_select_status()

    def test_checkbox_check_uncheck(self):
        print("Test started: checkbox")
        dyn_contr_page=DynamicControlPage(self.driver)

        self.driver.get(base_url + "dynamic_controls")
        assert dyn_contr_page.checkbox_select_status() == False
        dyn_contr_page.click_checkbox()
        time.sleep(2)
        assert dyn_contr_page.checkbox_select_status()
        dyn_contr_page.click_checkbox()
        time.sleep(2)
        assert dyn_contr_page.checkbox_select_status() == False

    # TODO:tutaj poprawic
    def test_checkbox_remove(self):
        print("Test started: checkbox")
        dyn_contr_page=DynamicControlPage(self.driver)

        self.driver.get(base_url + "dynamic_controls")
        assert dyn_contr_page.checkbox_display_status()
        dyn_contr_page.click_remove_btn()
        # time.sleep(3)
        assert dyn_contr_page.assert_checkbox_dissappeared() == True

    # TODO:tutaj poprawic
    def test_checkbox_remove_add(self):
        print("Test started: checkbox")
        dyn_contr_page=DynamicControlPage(self.driver)

        self.driver.get(base_url + "dynamic_controls")
        assert dyn_contr_page.checkbox_display_status()
        dyn_contr_page.click_remove_btn()
        assert dyn_contr_page.assert_checkbox_dissappeared()
        dyn_contr_page.click_add_btn()
        assert dyn_contr_page.assert_checkbox_appeared()

    def test_input_disabled(self):
        print("Test started: input")
        dyn_contr_page = DynamicControlPage(self.driver)

        self.driver.get(base_url + "dynamic_controls")
        assert dyn_contr_page.input_field_enabled() == False

    def test_input_enable(self):
        print("Test started: input")
        dyn_contr_page = DynamicControlPage(self.driver)

        self.driver.get(base_url + "dynamic_controls")
        assert dyn_contr_page.input_field_enabled() == False
        dyn_contr_page.click_enable_btn()
        dyn_contr_page.input_send_keys("random")
        assert dyn_contr_page.assert_input_field_enabled()
        time.sleep(3)

    def test_input_enable_disable(self):
        print("Test started: input")
        dyn_contr_page = DynamicControlPage(self.driver)

        self.driver.get(base_url + "dynamic_controls")
        assert dyn_contr_page.input_field_enabled() == False
        dyn_contr_page.click_enable_btn()
        dyn_contr_page.input_send_keys("some_text123")
        assert dyn_contr_page.assert_input_field_enabled()
        dyn_contr_page.click_disable_btn()
        assert dyn_contr_page.assert_input_field_disabled()
