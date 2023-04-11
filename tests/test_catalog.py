import pytest
from pages.CatalogPage import CatalogPage
import pytest_check as check
import allure


@allure.title("Check if all elements are present on Catalog Page")
@pytest.mark.parametrize(
    "catalog", ["/desktops", "/camera", "/mp3-players", "/laptop-notebook"]
)
def test_catalog_page_elements_presence(browser, base_url, catalog):
    catalog_page = CatalogPage(browser, base_url + catalog)
    catalog_page.open_page()

    check.not_equal(
        catalog_page.verify_empty_catalog_msg_el().text,
        "There are no products to list in this category.",
    )
    check.equal(
        catalog_page.verify_grid_view_btn_el().get_attribute("data-original-title"),
        "Grid",
    )
    check.equal(
        catalog_page.verify_list_view_btn_el().get_attribute("data-original-title"),
        "List",
    )
    check.is_true(catalog_page.verify_product_thumb_el(), True)
    check.is_in("Product Compare", catalog_page.verify_product_compare_el().text)
