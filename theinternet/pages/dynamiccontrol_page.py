from page_objects import PageObject, PageElement

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from theinternet.config.config import explicit_timeout


class DynamicControlPage(PageObject):
    # locators
    _checbox_loc = "//input[@type='checkbox']"
    _checkbox_btn_loc = "#checkbox-example > button"
    _message_loc = "message"
    _input_field_loc = "#input-example>input"
    _input_btn_loc = "#input-example > button"
    _gone_loc = '//p[contains(text(),"gone")]'
    _back_loc = '//p[contains(text(),"back")]'

    # elements
    checkbox_box = PageElement(xpath=_checbox_loc)
    checkbox_btn = PageElement(css=_checkbox_btn_loc)
    message_txt = PageElement(id_=_message_loc)
    input_field = PageElement(css=_input_field_loc)
    input_btn = PageElement(css=_input_btn_loc)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        print("Created DynamicControl Page")

    def input_field_enabled(self):
        # print("input field {}".format(self.input_field.is_enabled()))
        return self.input_field.is_enabled()

    def click_enable_btn(self):
        self.input_btn.click()
        self.wait_input_interactible()

    def click_disable_btn(self):
        self.input_btn.click()
        self.wait_input_interactible()

    def input_send_keys(self, typetext):
        self.input_field = typetext

    def wait_input_interactible(self):
        wait = WebDriverWait(self.driver, explicit_timeout)
        w = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, self._input_btn_loc)))
        # print("Waiting")
        return w

    def wait_for_element_presence(self, locator):
        try:
            print("Waiting wait_for_ element_presence")
            WebDriverWait(self.driver, explicit_timeout).until\
                (ec.presence_of_element_located((By.XPATH, locator)))
            # print("Element present")
            return True
        except (NoSuchElementException):
            # print("No such element when checking presence")
            return False

    def click_checkbox(self):
        self.checkbox_box.click()

    def click_remove_btn(self):
        print("Clicked remove")
        self.checkbox_btn.click()
        # print(self.return_message_txt())

    def click_add_btn(self):
        self.checkbox_btn.click()

    def checkbox_select_status(self):
        return self.checkbox_box.is_selected()

    def return_message_txt(self):
        return self.message_txt.text

    def checkbox_display_status(self):
        return self.checkbox_box.is_displayed()

    def is_checkbox_present(self):
        try:
            self.checkbox_btn.is_displayed()
            print("Checkbox is present")
            return True
        except NoSuchElementException:
            print("Checkbox not present")
            return False

    def assert_checkbox_dissappeared(self):
        return self.wait_for_element_presence(self._gone_loc)

    def assert_checkbox_appeared(self):
        return self.wait_for_element_presence(self._back_loc)

    def assert_input_field_enabled(self):
        if self.input_field_enabled() and self.return_message_txt() == "It's enabled!":
            return True
        else:
            return False

    def assert_input_field_disabled(self):
        if self.input_field_enabled() == False and self.return_message_txt() == "It's disabled!":
            return True
        else:
            return False
