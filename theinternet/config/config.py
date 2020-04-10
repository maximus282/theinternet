import platform

os_name = platform.system()
if os_name == "Windows":
    chromedriver_path="../driver/windows/chromedriver"
if os_name == "Linux":
    chromedriver_path = "../driver/linux/chromedriver"
if os_name == "Darwin":
    chromedriver_path = "../driver/mac/chromedriver"

base_url="https://the-internet.herokuapp.com/"
resource_url={
    "login_url":"login",
    "geolocation_url":"geolocation",
    "dyn_contr_url":"dynamic_controls",
    "jsalerts_url":"javascript_alerts"
}

implicit_timeout=10
explicit_timeout=10
