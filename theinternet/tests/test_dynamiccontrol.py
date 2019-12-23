import time

import pytest
from selenium import webdriver

import unittest
from theinternet.pages.dynamiccontrol_page import DynamicControlPage

from theinternet.config.config import base_url,resource_url
from theinternet.tests.basetest import BaseTest


@pytest.fixture(scope="function")
def get_url():
    return base_url+str(resource_url.get("dyn_contr_url"))


class TestDynContrPage(BaseTest):


    #test_data
    data=[("mytext1"),(""),(123)]

    def test_checkbox_check(self,get_url):
        dyn_contr_page=DynamicControlPage(self.driver)

        self.driver.get(get_url)
        assert dyn_contr_page.checkbox_select_status() == False
        dyn_contr_page.click_checkbox()
        time.sleep(2)
        assert dyn_contr_page.checkbox_select_status()

    def test_checkbox_check_uncheck(self,get_url):
        dyn_contr_page=DynamicControlPage(self.driver)

        self.driver.get(get_url)
        assert dyn_contr_page.checkbox_select_status() == False
        dyn_contr_page.click_checkbox()
        assert dyn_contr_page.checkbox_select_status()
        dyn_contr_page.click_checkbox()
        assert dyn_contr_page.checkbox_select_status() == False

    def test_checkbox_remove(self,get_url):
        dyn_contr_page=DynamicControlPage(self.driver)

        self.driver.get(get_url)
        assert dyn_contr_page.checkbox_display_status()
        dyn_contr_page.click_remove_btn()
        assert dyn_contr_page.assert_checkbox_dissappeared()

    def test_checkbox_remove_add(self,get_url):
        dyn_contr_page=DynamicControlPage(self.driver)

        self.driver.get(get_url)
        assert dyn_contr_page.checkbox_display_status()
        dyn_contr_page.click_remove_btn()
        assert dyn_contr_page.assert_checkbox_dissappeared()
        dyn_contr_page.click_add_btn()
        assert dyn_contr_page.assert_checkbox_appeared()

    def test_input_disabled(self,get_url):
        dyn_contr_page = DynamicControlPage(self.driver)

        self.driver.get(get_url)
        assert dyn_contr_page.input_field_enabled() == False

    @pytest.mark.parametrize("data", data)
    def test_input_enable(self,get_url,data):
        dyn_contr_page = DynamicControlPage(self.driver)

        self.driver.get(get_url)
        assert dyn_contr_page.input_field_enabled() == False
        dyn_contr_page.click_enable_btn()
        dyn_contr_page.input_send_keys(data)
        assert dyn_contr_page.assert_input_field_enabled()
        time.sleep(3)

    @pytest.mark.parametrize("data", data)
    def test_input_enable_disable(self,get_url,data):
        dyn_contr_page = DynamicControlPage(self.driver)

        self.driver.get(get_url)
        assert dyn_contr_page.input_field_enabled() == False
        dyn_contr_page.click_enable_btn()
        dyn_contr_page.input_send_keys(data)
        assert dyn_contr_page.assert_input_field_enabled()
        dyn_contr_page.click_disable_btn()
        assert dyn_contr_page.assert_input_field_disabled()
