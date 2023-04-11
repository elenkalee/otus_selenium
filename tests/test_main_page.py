from pages.MainPage import MainPage
import pytest_check as check
import allure


class TestMainPage:

    @allure.title("Check if all elements are present on Main Page")
    def test_main_page_elements_presence(self, browser, base_url):
        main_page = MainPage(browser, base_url)
        main_page.open_page()
        check.equal(
            main_page.verify_search_input_el().get_attribute("class"), "input-group"
        )
        check.equal(main_page.verify_currency_el().get_attribute("method"), "post")
        check.is_in("Your Store © ", main_page.verify_footer_el().text)
        check.is_in("Software", main_page.verify_main_menu_el().text)
        check.equal(
            main_page.verify_cart_btn_el().get_attribute("data-toggle"), "dropdown"
        )

    @allure.title("Check if possible to change currency from drop-down menu")
    def test_change_currency(self, browser, base_url):
        """Переключение валют из верхнего меню опенкарта"""

        main_page = MainPage(browser, base_url)
        main_page.open_page()
        main_page.change_currency("GBP")
        assert main_page.CURRENCY["GBP"] == main_page.current_currency_sign
