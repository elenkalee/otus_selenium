from .BasePage import BasePage
from selenium.webdriver.common.by import By
from data import TEST_USER


class RegisterUser(BasePage):
    TITLE_REGISTER_ACC = (By.CSS_SELECTOR, ".col-sm-9 h1")
    RADIO_BTN_NO = (By.CSS_SELECTOR, "label:nth-child(2) > input[type=radio]")
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    LIST_GROUP_TAB = (By.CSS_SELECTOR, ".list-group")
    REGISTERED_USER_WARNING = (By.CSS_SELECTOR, ".col-sm-9 p")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    INPUT_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    POLICY_CHECKBOX = (By.CSS_SELECTOR, '[type="checkbox"]')
    SUBMIT_BTN = (By.CSS_SELECTOR, '[type="submit"]')
    SUCCESS_REGISTRATION = (By.CSS_SELECTOR, "#common-success")

    def open_page(self):
        return self.driver.get(self.base_url + "/index.php?route=account/register")

    def verify_title_register_acc_el(self):
        return self._verify_element_visibility(self.TITLE_REGISTER_ACC)

    def verify_radio_btn_no_el(self):
        return self._verify_element_visibility(self.RADIO_BTN_NO)

    def verify_input_firstname_el(self):
        return self._verify_element_visibility(self.INPUT_FIRSTNAME)

    def verify_list_group_tab_el(self):
        return self._verify_elements_visibility(self.LIST_GROUP_TAB)

    def verify_registered_user_warning_el(self):
        return self._verify_element_visibility(self.REGISTERED_USER_WARNING)

    def fill_register_user_form(self):
        self._input_fill(self.INPUT_FIRSTNAME, TEST_USER["firstname"])
        self._input_fill(self.INPUT_LASTNAME, TEST_USER["lastname"])
        self._input_fill(self.INPUT_EMAIL, TEST_USER["email"])
        self._input_fill(self.INPUT_TELEPHONE, TEST_USER["telephone"])
        self._input_fill(self.INPUT_PASSWORD, TEST_USER["password"])
        self._input_fill(self.INPUT_CONFIRM, TEST_USER["password"])
        self._find_and_click_element(self.POLICY_CHECKBOX)
        self._find_and_click_element(self.SUBMIT_BTN)
        self._verify_element_visibility(self.SUCCESS_REGISTRATION)
