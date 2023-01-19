from .BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    TAB_DESCRIPTION = (By.CSS_SELECTOR, 'a[href^="#tab-description"]')
    TAB_REVIEW = (By.CSS_SELECTOR, 'a[href^="#tab-review"]')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#button-cart")
    PRODUCT_NAME_TITLE = (By.CSS_SELECTOR, "#content .col-sm-4 h1")
    PRODUCT_NAME_TAB = (By.CSS_SELECTOR, "#product-product > ul > li:nth-child(2) > a")
    WISHLIST_BTN = (
        By.CSS_SELECTOR,
        "div.col-sm-4 > div.btn-group > button:nth-child(1)",
    )

    def verify_tab_description_el(self):
        return self._verify_element_visibility(self.TAB_DESCRIPTION)

    def verify_tab_review_el(self):
        return self._verify_element_visibility(self.TAB_REVIEW)

    def verify_add_to_cart_btn_el(self):
        return self._verify_element_visibility(self.ADD_TO_CART_BTN)

    def verify_product_name_tab_el(self):
        product_name_tab_el = self._verify_element_visibility(self.PRODUCT_NAME_TAB)
        product_name_el = self._verify_element_visibility(self.PRODUCT_NAME_TITLE)
        assert product_name_tab_el.text == product_name_el.text

    def verify_wishlist_btn_el(self):
        return self._verify_element_visibility(self.WISHLIST_BTN)
