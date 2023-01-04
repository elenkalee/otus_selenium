from .BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginAdminPage(BasePage):
    LOGIN_DETAILS_MSG = (By.CSS_SELECTOR, ".panel-title")
    SUBMIT_BTN = (By.CSS_SELECTOR, '[type="submit"]')
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, 'a[href*="forgotten"]')
    MENU_CATALOG_TAB = (By.CSS_SELECTOR, "#menu-catalog")
    MENU_CATALOG_PRODUCTS_TAB = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2) > a")
    PRODUCTS_LIST = (By.CSS_SELECTOR, "#form-product table")
    ADD_NEW_BTN = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, '[placeholder="Product Name"]')
    META_TAG_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")
    TAB_DATA = (By.CSS_SELECTOR, 'a[href="#tab-data"]')
    MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    SAVE_BTN = (By.CSS_SELECTOR, ".fa-save")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    DELETE_BTN = (By.CSS_SELECTOR, ".btn-danger")

    def open_page(self):
        return self.driver.get(self.base_url + "/admin")

    def verify_username_input_el(self):
        return self._verify_element_visibility(self.USERNAME_INPUT)

    def verify_password_input_el(self):
        return self._verify_element_visibility(self.PASSWORD_INPUT)

    def verify_forgot_password_link_el(self):
        return self._verify_element_visibility(self.FORGOT_PASSWORD_LINK)

    def verify_submit_btn_el(self):
        return self._verify_element_visibility(self.SUBMIT_BTN)

    def verify_login_details_msg_el(self):
        return self._verify_element_visibility(self.LOGIN_DETAILS_MSG)

    def login_as_admin(self):
        self._input_fill(self.USERNAME_INPUT, "user")
        self._input_fill(self.PASSWORD_INPUT, "bitnami")
        self._verify_element_visibility(self.SUBMIT_BTN).click()

    def open_list_of_products(self):
        self._find_and_click_element(self.MENU_CATALOG_TAB)
        self._find_and_click_element(self.MENU_CATALOG_PRODUCTS_TAB)

    def get_products_list(self):
        products_list = self._verify_element_visibility(self.PRODUCTS_LIST)
        return products_list.text

    def add_new_product(self, name):
        self._find_and_click_element(self.ADD_NEW_BTN)
        self._input_fill(self.PRODUCT_NAME_INPUT, name)
        self._input_fill(self.META_TAG_TITLE_INPUT, "test test test")
        self._find_and_click_element(self.TAB_DATA)
        self._input_fill(self.MODEL_INPUT, "test")
        self._find_and_click_element(self.SAVE_BTN)
        self._verify_element_visibility(self.SUCCESS_ALERT)

    def delete_product_as_admin(self):
        last_product = self.get_last_product()
        checkbox = last_product.find_element(By.TAG_NAME, "input")
        checkbox.click()
        self._find_and_click_element(self.DELETE_BTN)
        self.accept_delete_alert()
        self._verify_element_visibility(self.SUCCESS_ALERT)

    def get_last_product(self):
        products_list = (
            self._verify_element_visibility(self.PRODUCTS_LIST)
        ).find_elements(By.TAG_NAME, "tr")
        return products_list[len(products_list) - 1]

    def accept_delete_alert(self):
        confirm_alert = self.driver.switch_to.alert
        confirm_alert.accept()
