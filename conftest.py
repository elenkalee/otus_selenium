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
    parser.addoption(
        "--driver_folder",
        default="/Users/elenalee/Desktop/PycharmProjects/otus_selenium/drivers_mac",
    )
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", action="store", default="http://192.168.0.101:8081")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    url = request.config.getoption("--url")
    _browser = request.config.getoption("--browser")
    driver_folder = request.config.getoption("--driver_folder")
    headless = request.config.getoption("--headless")
    driver = None

    if _browser == "chrome":
        service = ChromiumService(executable_path=f"{driver_folder}\\chromedriver")
        options = ChromiumOptions()
        options.headless = headless
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(service=service, options=options)

    elif _browser == "firefox" or _browser == "ff":
        service = FFService(executable_path=f"{driver_folder}\\geckodriver")
        options = FirefoxOptions()
        options.headless = headless
        driver = webdriver.Firefox(service=service, options=options)

    elif _browser == "msedge" or _browser == "edge":
        service = EdgeService(executable_path=f"{driver_folder}\\msedgedriver")
        options = EdgeOptions()
        options.headless = headless
        driver = webdriver.Edge(service=service, options=options)

    elif _browser == "yandex" or _browser == "ya":
        service = ChromiumService(executable_path=f"{driver_folder}\\yandexdriver")
        options = ChromiumOptions()
        options.headless = headless
        driver = webdriver.Chrome(service=service, options=options)

    else:
        raise ValueError("Browser is not supported")

    request.addfinalizer(driver.quit)

    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)

    return driver
