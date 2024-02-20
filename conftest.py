import os
import pytest
from selenium import webdriver

website = "https://demo-opencart.ru"

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Driver not supported")

    driver.get(website)
    request.addfinalizer(driver.quit)

    return driver
