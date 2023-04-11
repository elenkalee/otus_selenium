from pages.RegisterPage import RegisterUser
import pytest_check as check
import allure


class TestRegisterUser:
    @allure.title("Check if all elements are present on User Register Page")
    def test_register_user_page_elements_presence(self, browser, base_url):
        register_user = RegisterUser(browser, base_url)
        register_user.open_page()

        check.equal(
            register_user.verify_title_register_acc_el().text, "Register Account"
        )
        check.equal(
            register_user.verify_registered_user_warning_el().text,
            "If you already have an account with us, please login at the login page.",
        )
        check.equal(
            register_user.verify_input_firstname_el().get_attribute("placeholder"),
            "First Name",
        )
        check.equal(
            register_user.verify_radio_btn_no_el().get_attribute("checked"), "true"
        )
        check.equal(len(register_user.verify_list_group_tab_el()), 1)

    @allure.title("Check if possible to register a new user")
    def test_register_new_user(self, browser, base_url):
        """Регистрация нового пользователя в магазине опенкарта"""
        register_user = RegisterUser(browser, base_url)
        register_user.open_page()
        assert browser.title == "Register Account"
