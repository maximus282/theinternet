import time

import pytest
from selenium import webdriver

import unittest
from theinternet.pages.geolocation_page import GeolocationPage

from theinternet.config.config import base_url
from theinternet.tests.basetest import BaseTest


class TestGeolocationPage(BaseTest):

    def test_get_geolocation(self):
        print("Test started: get geolocation")
        geolocation_page=GeolocationPage(self.driver)

        self.driver.get(base_url + "geolocation")
        geolocation_page.click_whereami()
        assert geolocation_page.assert_coordinates_presence() is True
        geolocation_page.display_location()


        # assert "You logged into a secure area!" in login_page.displayed_flash_message()