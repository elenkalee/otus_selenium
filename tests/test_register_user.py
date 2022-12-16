from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


def test_register_user_page_elements_presence(browser, base_url):
    browser.get(base_url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 3)

    title_register_acc_el = wait.until(
        EC.visibility_of_element_located(title_register_acc)
    )
    assert title_register_acc_el.text == "Register Account"

    registered_user_warning_el = wait.until(
        EC.visibility_of_element_located(registered_user_warning)
    )
    assert (
        registered_user_warning_el.text
        == "If you already have an account with us, please login at the login page."
    )

    input_firstname_el = wait.until(EC.visibility_of_element_located(input_firstname))
    assert input_firstname_el.get_attribute("placeholder") == "First Name"

    radio_btn_NO_el = wait.until(EC.visibility_of_element_located(radio_btn_NO))
    assert radio_btn_NO_el.get_attribute("checked") == "true"

    list_group_tab_el = wait.until(EC.presence_of_all_elements_located(list_group_tab))
    assert len(list_group_tab_el) == 1
