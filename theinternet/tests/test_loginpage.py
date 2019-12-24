import pytest

from theinternet.pages.login_page import Loginpage
from theinternet.pages.secure_page import SecurePage

from theinternet.config.config import base_url,resource_url
from theinternet.tests.basetest import BaseTest


@pytest.fixture(scope="function")
def get_url():
    return base_url+str(resource_url.get("login_url"))


class TestLoginPage(BaseTest):

    #test_data
    valid_credentials=[("tomsmith","SuperSecretPassword!")]
    invalid_password_credentials=[("tomsmith","wrongpassword"),("tomsmith","")]
    invalid_username_credentials=[("johndoe","johnspassword"),("Tomsmith","SuperSecretPassword!"),("",""),("","anypassword")]

    @pytest.mark.parametrize("user,password", valid_credentials)
    def test_my_valid_login(self,user,password,get_url):

        login_page = Loginpage(self.driver)
        secure_page = SecurePage(self.driver)

        self.driver.get(get_url)
        login_page.log_into_app(user, password)
        assert "You logged into a secure area!" in secure_page.displayed_flash_message()

    @pytest.mark.parametrize("user,password", valid_credentials)
    def test_valid_login_logout(self,user,password,get_url):
        login_page = Loginpage(self.driver)
        secure_page = SecurePage(self.driver)

        self.driver.get(get_url)

        login_page.log_into_app(user,password)
        # print (login_page.displayed_flash_message())
        assert "You logged into a secure area!" in secure_page.displayed_flash_message()
        # print (login_page.displayed_flash_message())
        secure_page.click_logout()
        # print (login_page.displayed_flash_message())
        assert "You logged out of the secure area!" in login_page.displayed_flash_message()


    @pytest.mark.parametrize("user,password", invalid_password_credentials )
    def test_invalid_password(self,user,password,get_url):

        login_page = Loginpage(self.driver)

        self.driver.get(get_url)
        login_page.log_into_app(user,password)
        assert "Your password is invalid!" in login_page.displayed_flash_message()

    @pytest.mark.parametrize("user,password", invalid_username_credentials )
    def test_invalid_username(self,user,password,get_url):

        login_page = Loginpage(self.driver)

        self.driver.get(get_url)
        login_page.log_into_app(user,password)
        assert "Your username is invalid!" in login_page.displayed_flash_message()



