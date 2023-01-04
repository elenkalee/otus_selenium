import pytest
from pages.CatalogPage import CatalogPage


@pytest.mark.parametrize(
    "catalog", ["/desktops", "/camera", "/mp3-players", "/laptop-notebook"]
)
def test_catalog_page_elements_presence(browser, base_url, catalog):
    """Переделаны тесты из 1 задания.
    Пока оставила такие же assertы, хотела применить библиотеку softtest, но не получилось"""
    catalog_page = CatalogPage(browser, base_url + catalog)
    catalog_page.open_page()

    assert (
        catalog_page.verify_empty_catalog_msg_el().text
        != "There are no products to list in this category."
    )
    assert (
        catalog_page.verify_grid_view_btn_el().get_attribute("data-original-title")
        == "Grid"
    )
    assert (
        catalog_page.verify_list_view_btn_el().get_attribute("data-original-title")
        == "List"
    )
    assert catalog_page.verify_product_thumb_el()
    assert "Product Compare" in catalog_page.verify_product_compare_el().text
