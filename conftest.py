from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromiumOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.edge.service import Service as EdgeService

from selenium import webdriver
import pytest
import logging
import datetime


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", action="store", default="http://192.168.43.157:8081")
    parser.addoption(
        "--driver_folder",
        default="/Users/elenalee/PycharmProjects/drivers",
    )

    parser.addoption("--browser", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.157")
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")
    driver_folder = request.config.getoption("--driver_folder")

    browser = request.config.getoption("--browser")
    driver = None
    executor = request.config.getoption("--executor")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger('simple_example')
    file_handler = logging.FileHandler("spam.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel("DEBUG")
    test_name = request.node.name

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))
    if browser == "chrome":
        service = ChromiumService(executable_path=f"{driver_folder}\\chromedriver")
        options = ChromiumOptions()
        options.headless = headless
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox" or browser == "ff":
        service = FFService(executable_path=f"{driver_folder}\\geckodriver")
        options = FirefoxOptions()
        options.headless = headless
        driver = webdriver.Firefox(service=service, options=options)

    elif browser == "msedge" or browser == "edge":
        service = EdgeService(executable_path=f"{driver_folder}\\msedgedriver")
        options = EdgeOptions()
        options.headless = headless
        driver = webdriver.Edge(service=service, options=options)

    elif browser == "yandex" or browser == "ya":
        service = ChromiumService(executable_path=f"{driver_folder}\\yandexdriver")
        options = ChromiumOptions()
        options.headless = headless
        driver = webdriver.Chrome(service=service, options=options)

    else:
        raise ValueError("Browser not supported!")

    driver.log_level = log_level
    driver.logger = logger

    logger.info("===> Test {} started at {}".format(test_name, datetime.datetime.now()))

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)

    return driver
