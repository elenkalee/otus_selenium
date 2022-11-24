from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

    parser.addoption("--driver_folder", default="C:\\drivers")

    parser.addoption("--headless", action="store_true")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    _driver_folder = request.config.getoption("--driver_folder")
    _headless = request.config.getoption("--headless")

    driver = None
    if _browser == "firefox" or _browser == "ff":
        options = FirefoxOptions()
        options.headless = _headless
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox(
            executable_path=f"{_driver_folder}\\geckodriver.exe", options=options
        )

    elif _browser == "chrome":
        options = ChromeOptions()
        options.headless = _headless
        driver = webdriver.Chrome(
            executable_path=f"{_driver_folder}\\chromedriver.exe", options=options
        )

    elif _browser == "msedge" or _browser == "edge":
        options = EdgeOptions()
        options.headless = _headless
        driver = webdriver.Edge(
            executable_path=f"{_driver_folder}\\msedgedriver.exe", options=options
        )

    elif _browser == "yandex" or _browser == "ya":
        options = ChromeOptions()
        options.headless = _headless
        driver = webdriver.Chrome(
            executable_path=f"{_driver_folder}\\yandexdriver.exe", options=options
        )

    driver.maximize_window()
    yield driver
    driver.close()
