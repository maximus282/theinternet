from page_objects import PageObject, PageElement
import time


class AlertPage(PageObject):

    #locators
    _js_alert_loc="//button[text() = \"Click for JS Alert\"]"
    _js_conf_loc="//button[text() = \"Click for JS Confirm\"]"
    _js_prompt_loc="//button[text() = \"Click for JS Prompt\"]"
    _result_loc="result"

    #elements
    js_alert_btn=PageElement(xpath=_js_alert_loc)
    js_conf_btn=PageElement(xpath=_js_conf_loc)
    js_prompt_btn=PageElement(xpath=_js_prompt_loc)
    result=PageElement(id_=_result_loc)

    #messages
    alert_ok_msg="You successfuly clicked an alert"
    conf_ok_msg="You clicked: Ok"
    conf_dismiss_msg="You clicked: Cancel"
    prompt_msg="You entered: "
    prompt_dismiss_msg="You entered: null"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        print("Created JavaScript Alert page")

    def click_alert_btn(self):
        self.js_alert_btn.click()

    def click_conf_btn(self):
        self.js_conf_btn.click()

    def click_prompt_btn(self):
        self.js_prompt_btn.click()

    def handle_popup(self):
        alert_popup = self.driver.switch_to.alert
        alert_msg = alert_popup.text
        # print("Alert message: {}".format(alert_msg))
        return alert_popup

    def accept_popup(self):
        self.handle_popup().accept()

    def dismiss_popup(self):
        self.handle_popup().dismiss()

    def sendkeys_popup(self,text):
        self.handle_popup().send_keys(str(text))
        return text

    def display_return_msg(self):
        return self.result.text
