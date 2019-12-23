from page_objects import PageObject, PageElement
from selenium import webdriver
import time


class Loginpage(PageObject):

    #locators
    _username_loc="username"
    _password_loc="password"
    _loginbtn_loc="#login > button > i"
    _flash_message_loc = "flash"

    #elements
    username = PageElement(id_=_username_loc)
    password = PageElement(id_=_password_loc)
    login_btn = PageElement(css=_loginbtn_loc)
    flash_message=PageElement(id_=_flash_message_loc)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        print("Created LoginPage")

    def enter_username(self,user):
        self.username.clear()
        self.username=user

    def enter_password(self,passwd):
        self.password.clear()
        self.password=passwd

    def click_login(self):
        self.login_btn.click()

    def log_into_app(self,account,password):
        print("Logging into app")
        self.enter_username(account)
        self.enter_password(password)
        self.click_login()

    def displayed_flash_message(self):
        return self.flash_message.text

    # def assert_flash_message(self):
    #     assert "You logged out of the secure area!" in self.displayed_flash_message()


####################################################


# base_url="http://the-internet.herokuapp.com/login"
# driver = webdriver.Firefox(executable_path="C:\\Users\\pl90636\\PycharmProjects\\seleniumwd2\\lib\\geckodriver.exe")
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get(base_url)
#
# sp = SecurePage(driver)
# print(driver.current_url)
# assert sp.valid_login_message(), True
#
# time.sleep(3)
# driver.quit()

