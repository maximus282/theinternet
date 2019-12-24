from page_objects import PageObject, PageElement

class SecurePage(PageObject):

    #locators
    _logout_btn_loc="#content > div > a"
    _flash_message_loc="flash"

    #elements
    logout_btn=PageElement(css= _logout_btn_loc)
    flash_message=PageElement(id_=_flash_message_loc)

    # messages for assert
    success_login_msg = "You logged into a secure area!"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        print("Created SecurePage")

    def get_flash_message_element(self):
        return self.flash_message

    def displayed_flash_message(self):
        return self.get_flash_message_element().text

    def click_logout(self):
        self.logout_btn.click()




