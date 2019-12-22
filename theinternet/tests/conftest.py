import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def setup(request):
    print("Running method - setUp")
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 1})
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path="../driver/chromedriver",options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    print("Running method - tearDown")
    # time.sleep(2)
    driver.delete_all_cookies()
    driver.quit()






