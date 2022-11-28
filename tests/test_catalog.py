import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

"""LOCATORS"""
catalog_name_title = (By.CSS_SELECTOR, "#content h2")
empty_catalog_msg = (By.CSS_SELECTOR, "#content p")
grid_view_btn = (By.CSS_SELECTOR, "#grid-view")
list_view_btn = (By.CSS_SELECTOR, "#list-view")
product_thumb = (By.CSS_SELECTOR, ".product-thumb")
product_compare = (By.CSS_SELECTOR, "#compare-total")


@pytest.mark.parametrize(
    "catalog", ["/desktops", "/camera", "/mp3-players", "/software", "/laptop-notebook"]
)
def test_catalog_page_elements_presence(browser, base_url, catalog):
    browser.get(base_url + catalog)
    wait = WebDriverWait(browser, 5)

    catalog_name_tab = (By.CSS_SELECTOR, f'.list-group > a[href*="{catalog}"]')
    catalog_name_tab_el = wait.until(EC.visibility_of_element_located(catalog_name_tab))
    catalog_name_title_el = wait.until(
        EC.visibility_of_element_located(catalog_name_title)
    )
    assert catalog_name_title_el.text in catalog_name_tab_el.text

    try:

        wait.until(EC.visibility_of_element_located(product_thumb))

        list_view_btn_el = wait.until(EC.visibility_of_element_located(list_view_btn))
        assert list_view_btn_el.get_attribute("data-original-title") == "List"

        grid_view_btn_el = wait.until(EC.visibility_of_element_located(grid_view_btn))
        assert grid_view_btn_el.get_attribute("data-original-title") == "Grid"

        product_compare_el = wait.until(
            EC.visibility_of_element_located(product_compare)
        )
        assert "Product Compare" in product_compare_el.text

    except TimeoutException:
        empty_catalog_msg_el = wait.until(
            EC.visibility_of_element_located(empty_catalog_msg)
        )
        assert (
            empty_catalog_msg_el.text
            == "There are no products to list in this category."
        )
