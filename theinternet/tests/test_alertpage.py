import time

import pytest

from theinternet.pages.alert_page import AlertPage

from theinternet.config.config import base_url,resource_url
from theinternet.tests.basetest import BaseTest

@pytest.fixture(scope="function")
def get_url():
    return base_url+str(resource_url.get("jsalerts_url"))

class TestAlertPage(BaseTest):

    #test_data
    data=[("mytext1"),(""),(123)]

    def test_jsalert_accept(self,get_url):
        """Scenario: Click JS Alert, confirm it"""

        alert_page=AlertPage(self.driver)

        self.driver.get(get_url)
        alert_page.click_alert_btn()
        alert_page.accept_popup()
        assert alert_page.display_return_msg() == alert_page.alert_ok_msg

    def test_jsconfirm_accept(self,get_url):
        """Scenario: Click JS Accept, confirm it"""

        alert_page = AlertPage(self.driver)

        self.driver.get(get_url)
        alert_page.click_conf_btn()
        alert_page.accept_popup()
        assert alert_page.display_return_msg() == alert_page.conf_ok_msg

    def test_jsconfirm_dismiss(self,get_url):
        """Scenario: Click JS Accept, dismiss it"""

        alert_page = AlertPage(self.driver)

        self.driver.get(get_url)
        alert_page.click_conf_btn()
        alert_page.dismiss_popup()
        assert alert_page.display_return_msg() == alert_page.conf_dismiss_msg

    @pytest.mark.parametrize("data_input", data)
    def test_jsprompt_accept(self,get_url,data_input):
        """Scenario: Click JS Prompt, send keys and accept it"""

        alert_page = AlertPage(self.driver)

        self.driver.get(get_url)
        alert_page.click_prompt_btn()
        alert_page.sendkeys_popup(data_input)
        alert_page.accept_popup()
        assert alert_page.display_return_msg() == (alert_page.prompt_msg + str(data_input)).rstrip()

    @pytest.mark.parametrize("data_input", data)
    def test_jsprompt_dismiss(self,get_url, data_input):
        """Scenario: Click JS Prompt, send keys and dismiss it"""

        alert_page = AlertPage(self.driver)

        self.driver.get(get_url)
        alert_page.click_prompt_btn()
        alert_page.sendkeys_popup(data_input)
        alert_page.dismiss_popup()
        assert alert_page.display_return_msg() == alert_page.prompt_dismiss_msg


