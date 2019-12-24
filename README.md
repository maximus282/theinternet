# theinternet
Project created in Python 3.7.4

To install project requirements please navigate to the root folder and install the below requirements using the below command:
>pip install -r requirements.txt

The tests should be executed in Chrome. The repository contains 2 Chrome drivers (version 79) for Linux and Windows.
Platform detection will happen automatically (config.py).

The project is created based on the Page object pattern.
Each Page is a different class.
Each Page is tested by a different Test class.
The tests suite is created in Pytest. This helps to manage and parametrize test cases.
To execute all tests please navigate to the: theinternet/tests folder and run:
>pytest

To execute test for a specific "page" please execute e.g.
>pytest test_geolocation.py

The requirements include the Allue Reports plugin for Pytest therefore if you want to generate an HTML report please run the below command:
>pytest --alluredir=%allure_result_folder%

To view the HTML reports run the below command (make sure you have allure installed and added to your PATH):
>allure server %allure_result_folder%

Author: Max S.