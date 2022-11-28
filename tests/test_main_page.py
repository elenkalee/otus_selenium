from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""LOCATORS"""
search_input = (By.CSS_SELECTOR, "#search")
main_menu = (By.CSS_SELECTOR, "#menu")
form_currency = (By.CSS_SELECTOR, "#form-currency")
footer_rigths = (By.CSS_SELECTOR, "footer>div>p")
cart_btn = (By.CSS_SELECTOR, "#cart > button")


def test_main_page_elements_presence(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 3)

    currency_el = wait.until(EC.visibility_of_element_located(form_currency))
    assert currency_el.get_attribute("method") == "post"

    search_el = wait.until(EC.visibility_of_element_located(search_input))
    assert search_el.get_attribute("class") == "input-group"

    footer_rights_el = wait.until(EC.visibility_of_element_located(footer_rigths))
    assert "Your Store © " in footer_rights_el.text

    main_menu_el = wait.until(EC.visibility_of_element_located(main_menu))
    assert "Software" in main_menu_el.text, "Menu tab"

    cart_btn_el = wait.until(EC.visibility_of_element_located(cart_btn))
    assert cart_btn_el.get_attribute("data-toggle") == "dropdown"
