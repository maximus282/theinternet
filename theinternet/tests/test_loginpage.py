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
        """Scenario: open login page and click Login using valid credentials"""

        login_page = Loginpage(self.driver)
        secure_page = SecurePage(self.driver)

        self.driver.get(get_url)
        login_page.log_into_app(user, password)
        assert secure_page.success_login_msg in secure_page.displayed_flash_message()

    @pytest.mark.parametrize("user,password", valid_credentials)
    def test_valid_login_logout(self,user,password,get_url):
        """Scenario: open login page and click Login, on the next page click Logout"""

        login_page = Loginpage(self.driver)
        secure_page = SecurePage(self.driver)

        self.driver.get(get_url)
        login_page.log_into_app(user,password)
        assert secure_page.success_login_msg in secure_page.displayed_flash_message()
        secure_page.click_logout()
        assert login_page.success_logout_msg in login_page.displayed_flash_message()


    @pytest.mark.parametrize("user,password", invalid_password_credentials )
    def test_invalid_password(self,user,password,get_url):
        """Scenario: open login page and click Login using invalid password"""

        login_page = Loginpage(self.driver)

        self.driver.get(get_url)
        login_page.log_into_app(user,password)
        assert login_page.invalid_pass_msg in login_page.displayed_flash_message()

    @pytest.mark.parametrize("user,password", invalid_username_credentials )
    def test_invalid_username(self,user,password,get_url):
        """Scenario: open login page and click Login using invalid username"""

        login_page = Loginpage(self.driver)

        self.driver.get(get_url)
        login_page.log_into_app(user,password)
        assert login_page.invalid_user_msg in login_page.displayed_flash_message()



