from pages.MainPage import MainPage


class TestMainPage:
    def test_main_page_elements_presence(self, browser, base_url):
        """Переделаны тесты из 1 задания.
        Пока оставила такие же assertы, хотела применить библиотеку softtest, но пока не получилось"""
        main_page = MainPage(browser, base_url)
        main_page.open_page()
        assert (
            main_page.verify_search_input_el().get_attribute("class") == "input-group"
        )
        assert main_page.verify_currency_el().get_attribute("method") == "post"
        assert "Your Store © " in main_page.verify_footer_el().text
        assert "Software" in main_page.verify_main_menu_el().text
        assert main_page.verify_cart_btn_el().get_attribute("data-toggle") == "dropdown"

    def test_change_currency(self, browser, base_url):
        """Переключение валют из верхнего меню опенкарта"""

        main_page = MainPage(browser, base_url)
        main_page.open_page()
        main_page.change_currency("GBP")
        assert main_page.CURRENCY["GBP"] == main_page.current_currency_sign
