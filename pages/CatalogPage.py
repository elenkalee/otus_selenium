from .BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    CATALOG_NAME_TITLE = (By.CSS_SELECTOR, "#content h2")
    # CATALOG_NAME_TAB = (By.CSS_SELECTOR, f'.list-group > a[href*="{catalog}"]')

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

    def verify_catalog_name_title_el(self, catalog):
        catalog_name_title_el = self._verify_element_visibility(self.CATALOG_NAME_TITLE)
        catalog_name_tab_el = self._verify_element_visibility(self.CATALOG_NAME_TAB)
        assert catalog_name_title_el.text in catalog_name_tab_el.text
