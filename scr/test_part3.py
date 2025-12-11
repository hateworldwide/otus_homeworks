from scr.conftest import browser
from scr.page_objects.main_page import MainPage
from scr.page_objects.objects.admin_page import AdminPage

def test_login_as_admin(browser):
    admin_page = AdminPage(browser)
    admin_page.open()
    admin_page.login("user", "bitnami")
    admin_page.is_logout_link_visible()

def test_add_item_to_cart(browser):
    main_page = MainPage(browser)
    main_page.open()
    product = main_page.get_random_product()
    product_name = main_page.get_product_name(product)
    main_page.add_to_cart(product)
    cart_page = main_page.go_to_cart()
    item_in_cart_name = cart_page.get_item_name()
    assert item_in_cart_name == product_name

def test_change_currency(browser):
    main_page = MainPage(browser)
    main_page.open()
    old_currency = main_page.get_current_currency()
    old_prices = main_page.get_all_prices()
    new_currency = main_page.switch_to_different_currency()
    new_prices = main_page.get_all_prices()
    main_page.check_currencies(old_currency, new_currency)
    main_page.check_prices(new_currency, enumerate(zip(old_prices, new_prices)))

def test_currency_in_cart(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.add_to_cart(main_page.get_random_product())
    cart_page = main_page.go_to_cart()
    old_currency = cart_page.get_current_currency()
    old_prices = cart_page.get_all_prices()
    new_currency = cart_page.switch_to_different_currency()
    new_prices = cart_page.get_all_prices()
    cart_page.check_currencies(old_currency, new_currency)
    cart_page.check_prices(new_currency, enumerate(zip(old_prices, new_prices)))

def test_add_product(browser):
    admin_page = AdminPage(browser)
    admin_page.open()
    admin_page.login("user", "bitnami")
    admin_page.open_product_section()
    admin_page.open_add_product()
    admin_page.fill_required_fields()
    admin_page.submit()
    admin_page.is_success()

def test_delete_product(browser):
    admin_page = AdminPage(browser)
    admin_page.open()
    admin_page.login("user", "bitnami")
    admin_page.open_product_section()
    admin_page.delete_some_item()
    admin_page.is_success()

def test_register_client(browser):
    main_page = MainPage(browser)
    main_page.open()
    register_page = main_page.open_register()
    register_page.fill_fields()
    register_page.submit()
    register_page.is_success()