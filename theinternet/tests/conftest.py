import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from theinternet.config.config import implicit_timeout
from theinternet.config.config import chromedriver_path


@pytest.fixture(scope="function")
def setup(request):
    print("Running method - setUp")
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 1})
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=chromedriver_path,options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(implicit_timeout)
    request.cls.driver = driver

    yield
    print("Running method - tearDown")
    # time.sleep(2)
    driver.delete_all_cookies()
    driver.quit()






