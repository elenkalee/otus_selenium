import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""LOCATORS"""
tab_description = (By.CSS_SELECTOR, 'a[href^="#tab-description"]')
tab_review = (By.CSS_SELECTOR, 'a[href^="#tab-review"]')
add_to_cart_btn = (By.CSS_SELECTOR, "#button-cart")
product_name_title = (By.CSS_SELECTOR, "#content .col-sm-4 h1")
product_name_tab = (By.CSS_SELECTOR, "#product-product > ul > li:nth-child(2) > a")
wishlist_btn = (By.CSS_SELECTOR, "div.col-sm-4 > div.btn-group > button:nth-child(1)")


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
