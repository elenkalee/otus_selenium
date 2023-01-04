import pytest
from pages.ProductPage import ProductPage
import pytest_check as check


@pytest.mark.parametrize("product", ["/canon-eos-5d", "/hp-lp3065", "/htc-touch-hd"])
def test_product_page_elements_presence(browser, base_url, product):
    product_page = ProductPage(browser, base_url + product)
    product_page.open_page()

    check.is_in("Description", product_page.verify_tab_description_el().text)
    check.is_in("Reviews", product_page.verify_tab_review_el().text)
    check.is_in("Add to Cart", product_page.verify_add_to_cart_btn_el().text)
    product_page.verify_product_name_tab_el()
    check.equal(
        product_page.verify_wishlist_btn_el().get_attribute("data-original-title"),
        "Add to Wish List",
    )
