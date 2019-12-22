from page_objects import PageObject, PageElement
from selenium import webdriver
import time


class DynamicControlPage(PageObject):

    #locators
    _checbox_loc="#checkbox > input[type=checkbox]"
    _remove_btn_loc="#checkbox-example > button"
    _message_loc="#message"

    #elements
    checkbox_box=PageElement(css=_checbox_loc)
    remove_btn=PageElement(css=_remove_btn_loc)
    message_txt=PageElement(id_=_message_loc)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        print("Created DynamicControl Page")

    def click_checkbox(self):
        self.checkbox_box.click()

    def click_remove_btn(self):
        self.remove_btn.click()
        return DynamicControlPage(self.driver)

    def checkbox_select_status(self):
        return self.checkbox_box.is_selected()

    def checkbox_display_status(self):
        print(self.checkbox_box)
        print("Checbkox status " + str(self.checkbox_box.is_enabled()))
        return self.checkbox_box.is_enabled()


