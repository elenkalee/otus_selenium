from .BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    CATALOG_NAME_TITLE = (By.CSS_SELECTOR, "#content h2")
    EMPTY_CATALOG_MSG = (By.CSS_SELECTOR, "#content p")
    GRID_VIEW_BTN = (By.CSS_SELECTOR, "#grid-view")
    LIST_VIEW_BTN = (By.CSS_SELECTOR, "#list-view")
    PRODUCT_THUMB = (By.CSS_SELECTOR, ".product-thumb")
    PRODUCT_COMPARE = (By.CSS_SELECTOR, "#compare-total")

    def verify_empty_catalog_msg_el(self):
        return self._verify_element_visibility(self.EMPTY_CATALOG_MSG)

    def verify_grid_view_btn_el(self):
        return self._verify_element_visibility(self.GRID_VIEW_BTN)

    def verify_list_view_btn_el(self):
        return self._verify_element_visibility(self.LIST_VIEW_BTN)

    def verify_product_thumb_el(self):
        return self._verify_element_visibility(self.PRODUCT_THUMB)

    def verify_product_compare_el(self):
        return self._verify_element_visibility(self.PRODUCT_COMPARE)
