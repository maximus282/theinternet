from page_objects import PageObject, PageElement
from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class DynamicControlPage(PageObject):

    #locators
    _checbox_loc="#checkbox > input[type=checkbox]"
    _btn_loc="#checkbox-example > button"
    _message_loc="message"

    #elements
    checkbox_box=PageElement(css=_checbox_loc)
    remove_btn=PageElement(css=_btn_loc)
    add_btn=PageElement(css=_btn_loc)
    message_txt=PageElement(id_=_message_loc)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        print("Created DynamicControl Page")

    def click_checkbox(self):
        self.checkbox_box.click()

    def click_remove_btn(self):
        self.remove_btn.click()

    def click_add_btn(self):
        self.add_btn.click()

    def checkbox_select_status(self):
        return self.checkbox_box.is_selected()

    def return_message_txt(self):
        return self.message_txt.text

    def checkbox_display_status(self):
        return self.checkbox_box.is_displayed()

    def is_checkbox_present(self):
        try:
            self.checkbox_box
            print("Checkbox exists")
            return True
        except NoSuchElementException:
            print("Checkbox does not exist")
            return False

    def wait_checkbox_invisible(self):

        wait=WebDriverWait(self.driver,10)
        wait.until(ec.invisibility_of_element(self.checkbox_box))
        self.is_checkbox_present()

    def wait_checkbox_visible(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(ec.invisibility_of_element(self.checkbox_box))
            print("Element visible")
            return True
        except:
            print("Element not located")
            return False

    def assert_checkbox_dissappeared(self):
        if self.wait_checkbox_visible() == False and self.return_message_txt() == "It's gone!":
            print(self.wait_checkbox_visible())
            print(self.return_message_txt())
            return True
        else:
            return False

    def assert_checkbox_appeared(self):
        if self.wait_checkbox_visible() == True and self.return_message_txt() == "It's back!":
            print(self.wait_checkbox_invisible())
            print(self.return_message_txt())
            return True
        else:
            return False

