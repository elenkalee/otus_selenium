from selenium.webdriver.common.by import By

"""catalog page"""
catalog_name_title = (By.CSS_SELECTOR, "#content h2")
empty_catalog_msg = (By.CSS_SELECTOR, "#content p")
grid_view_btn = (By.CSS_SELECTOR, "#grid-view")
list_view_btn = (By.CSS_SELECTOR, "#list-view")
product_thumb = (By.CSS_SELECTOR, ".product-thumb")
product_compare = (By.CSS_SELECTOR, "#compare-total")

"""login admin page"""
login_details_msg = (By.CSS_SELECTOR, ".panel-title")
submit_btn = (By.CSS_SELECTOR, '[type="submit"]')
username_input = (By.CSS_SELECTOR, "#input-username")
password_input = (By.CSS_SELECTOR, "#input-password")
forgot_password_link = (By.CSS_SELECTOR, 'a[href*="forgotten"]')

"""main page"""
search_input = (By.CSS_SELECTOR, "#search")
main_menu = (By.CSS_SELECTOR, "#menu")
form_currency = (By.CSS_SELECTOR, "#form-currency")
footer_rigths = (By.CSS_SELECTOR, "footer>div>p")
cart_btn = (By.CSS_SELECTOR, "#cart > button")

"""product page"""
tab_description = (By.CSS_SELECTOR, 'a[href^="#tab-description"]')
tab_review = (By.CSS_SELECTOR, 'a[href^="#tab-review"]')
add_to_cart_btn = (By.CSS_SELECTOR, "#button-cart")
product_name_title = (By.CSS_SELECTOR, "#content .col-sm-4 h1")
product_name_tab = (By.CSS_SELECTOR, "#product-product > ul > li:nth-child(2) > a")
wishlist_btn = (By.CSS_SELECTOR, "div.col-sm-4 > div.btn-group > button:nth-child(1)")

"""register user page"""
title_register_acc = (By.CSS_SELECTOR, ".col-sm-9 h1")
radio_btn_NO = (By.CSS_SELECTOR, "label:nth-child(2) > input[type=radio]")
input_firstname = (By.CSS_SELECTOR, "#input-firstname")
list_group_tab = (By.CSS_SELECTOR, ".list-group")
registered_user_warning = (By.CSS_SELECTOR, ".col-sm-9 p")
