from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromiumOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.edge.service import Service as EdgeService

from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--driver_folder", default="C:\\drivers")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", action="store", default="http://192.168.43.169:8081")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    driver_folder = request.config.getoption("--driver_folder")
    headless = request.config.getoption("--headless")
    driver = None

    if _browser == "firefox" or _browser == "ff":
        service = FFService(executable_path=f"{driver_folder}\\geckodriver.exe")
        options = FirefoxOptions()
        options.headless = headless
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox(service=service, options=options)

    elif _browser == "chrome":
        service = ChromiumService(executable_path=f"{driver_folder}\\chromedriver.exe")
        options = ChromiumOptions()
        options.headless = headless
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(service=service, options=options)

    elif _browser == "msedge" or _browser == "edge":
        service = EdgeService(executable_path=f"{driver_folder}\\msedgedriver.exe")
        options = EdgeOptions()
        options.headless = headless
        driver = webdriver.Edge(service=service, options=options)

    elif _browser == "yandex" or _browser == "ya":
        service = ChromiumService(executable_path=f"{driver_folder}\\yandexdriver.exe")
        options = ChromiumOptions()
        options.headless = headless
        driver = webdriver.Chrome(service=service, options=options)

    else:
        raise ValueError("Browser is not supported")

    driver.maximize_window()
    yield driver
    driver.close()
