from pages.RegisterPage import RegisterUser


class TestRegisterUser:
    def test_register_user_page_elements_presence(self, browser, base_url):
        """Переделаны тесты из 1 задания.
        Пока оставила такие же assertы, хотела применить библиотеку softtest, но пока не получилось"""
        register_user = RegisterUser(browser, base_url)
        register_user.open_page()

        assert register_user.verify_title_register_acc_el().text == "Register Account"
        assert (
            register_user.verify_registered_user_warning_el().text
            == "If you already have an account with us, please login at the login page."
        )
        assert (
            register_user.verify_input_firstname_el().get_attribute("placeholder")
            == "First Name"
        )
        assert register_user.verify_radio_btn_no_el().get_attribute("checked") == "true"
        assert len(register_user.verify_list_group_tab_el()) == 1

    def test_register_new_user(self, browser, base_url):
        """Регистрация нового пользователя в магазине опенкарта"""
        register_user = RegisterUser(browser, base_url)
        register_user.open_page()
        assert browser.title == "Register Account"
