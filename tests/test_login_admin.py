from pages.LoginAdminPage import LoginAdminPage


class TestAdminPage:
    def test_login_admin_page_elements_presence(self, browser, base_url):
        """Переделаны тесты из 1 задания.
        Пока оставила такие же assertы, хотела применить библиотеку softtest, но пока не получилось"""
        login_page = LoginAdminPage(browser, base_url)
        login_page.open_page()
        assert login_page.verify_submit_btn_el().text == "Login"
        assert (
            login_page.verify_username_input_el().get_attribute("placeholder")
            == "Username"
        )
        assert (
            login_page.verify_password_input_el().get_attribute("placeholder")
            == "Password"
        )
        assert login_page.verify_forgot_password_link_el().text == "Forgotten Password"

    def test_login_as_admin(self, browser, base_url):
        """Авторизация в роли Администратора"""
        login_page = LoginAdminPage(browser, base_url)
        login_page.open_page()
        assert (
            "Please enter your login details."
            in login_page.verify_login_details_msg_el().text
        )

        login_page.login_as_admin()
        assert browser.title == "Dashboard"

    def test_add_new_product_as_admin(self, browser, base_url):
        """Добавление нового товара в разделе администратора"""
        login_page = LoginAdminPage(browser, base_url)
        login_page.open_page()
        login_page.login_as_admin()
        product_name = "Test Product"
        login_page.open_list_of_products()
        assert (
            product_name not in login_page.get_products_list()
        ), f"Product {product_name} already exists"
        login_page.add_new_product(product_name)
        assert (
            product_name in login_page.get_products_list()
        ), f"Product {product_name} wasn't found"

    def test_delete_product_as_admin(self, browser, base_url):
        """Удаление товара из списка в разделе администратора"""
        login_page = LoginAdminPage(browser, base_url)
        login_page.open_page()
        login_page.login_as_admin()
        product_name = "Test Product"
        login_page.open_list_of_products()
        assert (
            product_name in login_page.get_products_list()
        ), f"Product {product_name} wasn't found"
        login_page.delete_product_as_admin()
        assert (
            product_name not in login_page.get_products_list()
        ), f"Product {product_name} still exists"
