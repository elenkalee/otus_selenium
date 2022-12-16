from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


def test_login_admin_page_elements_presence(browser, base_url):
    browser.get(base_url + "/admin")
    wait = WebDriverWait(browser, 5)

    login_details_msg_el = wait.until(
        EC.visibility_of_element_located(login_details_msg)
    )
    assert "Please enter your login details." in login_details_msg_el.text

    submit_btn_el = wait.until(EC.visibility_of_element_located(submit_btn))
    assert submit_btn_el.text == "Login"

    username_input_el = wait.until(EC.visibility_of_element_located(username_input))
    assert username_input_el.get_attribute("placeholder") == "Username"

    password_input_el = wait.until(EC.visibility_of_element_located(password_input))
    assert password_input_el.get_attribute("placeholder") == "Password"

    forgot_password_link_el = wait.until(
        EC.visibility_of_element_located(forgot_password_link)
    )
    assert forgot_password_link_el.text == "Forgotten Password"
