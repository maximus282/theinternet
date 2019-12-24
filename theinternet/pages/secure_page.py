from page_objects import PageObject, PageElement

class SecurePage(PageObject):

    #locators
    _logout_btn_loc="#content > div > a"
    _flash_message_loc="flash"

    #elements
    logout_btn=PageElement(css= _logout_btn_loc)
    flash_message=PageElement(id_=_flash_message_loc)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        print("Created SecurePage")

    def displayed_flash_message(self):
        return self.flash_message.text

    def click_logout(self):
        self.logout_btn.click()




