import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler("spam.log")
        file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.driver.log_level)

    def open_page(self):
        self.logger.info(f"Open url {self.base_url}")
        return self.driver.get(self.base_url)

    def _verify_element_visibility(self, locator, time=2):
        self.logger.info(f"Check visibility of element {locator}")
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Element by locator: {locator} NOT found",
        )

    def _verify_elements_visibility(self, locator, time=2):
        self.logger.info(f"Check visibility of elements {locator}")
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_all_elements_located(locator),
            message=f"Elements by locator: {locator} NOT found",
        )

    def _verify_elements_presence(self, locator, time=2):
        self.logger.info(f"Check presence of element {locator}")
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Elements by locator: {locator} NOT present",
        )

    @allure.step("Click on element")
    def _find_and_click_element(self, locator):
        self.logger.info(f"Check visibility of element {locator} and click")
        element = self._verify_element_visibility(locator)
        element.click()

    def _input_fill(self, field, text):
        self.logger.info(f"Fill in {text} in {field} field")
        field = self._verify_element_visibility(field)
        field.click()
        field.clear()
        field.send_keys(text)
