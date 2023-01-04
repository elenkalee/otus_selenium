import pytest
from pages.ProductPage import ProductPage


@pytest.mark.parametrize("product", ["/canon-eos-5d", "/hp-lp3065", "/htc-touch-hd"])
def test_product_page_elements_presence(browser, base_url, product):
    """Переделаны тесты из 1 задания.
    Пока оставила такие же assertы, хотела применить библиотеку softtest, но пока не получилось"""
    product_page = ProductPage(browser, base_url + product)
    product_page.open_page()

    assert "Description" in product_page.verify_tab_description_el().text
    assert "Reviews" in product_page.verify_tab_review_el().text
    assert "Add to Cart" in product_page.verify_add_to_cart_btn_el().text
    product_page.verify_product_name_tab_el()
    assert (
        product_page.verify_wishlist_btn_el().get_attribute("data-original-title")
        == "Add to Wish List"
    )
