import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


@pytest.mark.parametrize(
    "product", ["/canon-eos-5d", "/hp-lp3065", "/samsung-galaxy-tab-10-1"]
)
def test_product_page_elements_presence(browser, base_url, product):
    browser.get(base_url + product)
    wait = WebDriverWait(browser, 3)

    description_tab_el = wait.until(EC.visibility_of_element_located(tab_description))
    assert "Description" in description_tab_el.text

    tab_review_el = wait.until(EC.visibility_of_element_located(tab_review))
    assert "Reviews" in tab_review_el.text

    add_to_cart_btn_el = wait.until(EC.element_to_be_clickable(add_to_cart_btn))
    assert "Add to Cart" in add_to_cart_btn_el.text

    product_name_tab_el = wait.until(EC.element_to_be_clickable(product_name_tab))
    product_name_el = wait.until(EC.visibility_of_element_located(product_name_title))
    assert product_name_tab_el.text == product_name_el.text

    wishlist_btn_el = wait.until(EC.visibility_of_element_located(wishlist_btn))
    assert wishlist_btn_el.get_attribute("data-original-title") == "Add to Wish List"
