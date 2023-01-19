from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open_page(self):
        return self.driver.get(self.base_url)

    def _verify_element_visibility(self, locator, time=2):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Element by locator: {locator} NOT found",
        )

    def _verify_elements_visibility(self, locator, time=2):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_all_elements_located(locator),
            message=f"Elements by locator: {locator} NOT found",
        )

    def _verify_elements_presence(self, locator, time=2):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Elements by locator: {locator} NOT present",
        )

    def _find_and_click_element(self, locator):
        element = self._verify_element_visibility(locator)
        element.click()

    def _input_fill(self, field, text):
        field = self._verify_element_visibility(field)
        field.click()
        field.clear()
        field.send_keys(text)
