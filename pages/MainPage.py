import softest

from .BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search")
    MAIN_MENU = (By.CSS_SELECTOR, "#menu")
    FOOTER_RIGTHS = (By.CSS_SELECTOR, "footer>div>p")
    CART_BTN = (By.CSS_SELECTOR, "#cart > button")
    CURRENCY_FORM = (By.CSS_SELECTOR, "#form-currency")
    CURRENCY = {"GBP": "£", "EUR": "€", "USD": "$"}
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#top .btn-group .dropdown-menu")
    CURRENCY_SIGN = (By.CSS_SELECTOR, "button.btn-link strong")

    def verify_search_input_el(self):
        return self._verify_element_visibility(self.SEARCH_INPUT)

    def verify_currency_el(self):
        return self._verify_element_visibility(self.CURRENCY_FORM)

    def verify_footer_el(self):
        return self._verify_element_visibility(self.FOOTER_RIGTHS)

    def verify_main_menu_el(self):
        return self._verify_element_visibility(self.MAIN_MENU)

    def verify_cart_btn_el(self):
        return self._verify_element_visibility(self.CART_BTN)

    @property
    def current_currency_sign(self):
        return self._verify_element_visibility(self.CURRENCY_SIGN).text

    def change_currency(self, value):
        self._find_and_click_element(self.CURRENCY_FORM)
        self._verify_element_visibility(self.CURRENCY_DROPDOWN)
        self._find_and_click_element(
            (By.CSS_SELECTOR, f".currency-select[name='{value}']")
        )
