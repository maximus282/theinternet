from page_objects import PageObject, PageElement

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

