import time

import pytest
from selenium import webdriver

import unittest
from theinternet.pages.login import Loginpage
from theinternet.pages.secure import SecurePage

baseURL="http://the-internet.herokuapp.com/"

@pytest.mark.usefixtures("setup")
class LoginTest(unittest.TestCase):

    def test_valid_login(self):
        print("Test started: valid login and logout")
        login_page = Loginpage(self.driver)
        secure_page = SecurePage(self.driver)

        self.driver.get(baseURL + "login")
        login_page.log_into_app("tomsmith", "SuperSecretPassword!")
        assert "You logged into a secure area!" in secure_page.displayed_flash_message()


    def test_valid_login_logout(self):
        print("Test started: valid login and logout")
        login_page = Loginpage(self.driver)
        secure_page = SecurePage(self.driver)

        self.driver.get(baseURL+"login")
        login_page.log_into_app("tomsmith","SuperSecretPassword!")
        assert "You logged into a secure area!" in secure_page.displayed_flash_message()
        secure_page.click_logout()
        assert "You logged out of the secure area!" in login_page.displayed_flash_message()


    def test_invalid_password(self):
        print("Test started: invalid password")

        login_page = Loginpage(self.driver)

        self.driver.get(baseURL+"login")
        login_page.log_into_app("tomsmith","wrongpassword!")
        assert "Your password is invalid!" in login_page.displayed_flash_message()


    def test_invalid_username(self):
        print("Test started: invalid username")

        login_page = Loginpage(self.driver)

        self.driver.get(baseURL + "login")
        login_page.log_into_app("tomsmith", "wrongpassword!")
        assert "Your password is invalid!" in login_page.displayed_flash_message()


    # @pytest.fixture(autouse=True)
    # def class_setup(self):
    #     self.lp = Loginpage(self.driver)
    #     self.sp = SecurePage(self.driver)


# def pytest_addoption(parser):
#     parser.addoption("--browser")
#     parser.addoption("--osType", help="Type of operating system")
#     parser.addoption("--vmType")


# @pytest.fixture(scope="session")
# def browser(request):
#     return request.config.getoption("--browser")
#
#
# @pytest.fixture(scope="session")
# def osType(request):
#     return request.config.getoption("--osType")

