from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from scr.conftest import browser
from scr.test_part2 import wait_element

def test_login_as_admin(browser):
    browser.get(f"http://{browser.base_url}/administration")
    actions = ActionChains(browser)
    username_input = browser.find_element(By.CSS_SELECTOR, 'input[name="username"]')
    password_input = browser.find_element(By.CSS_SELECTOR, 'input[id="input-password"]')
    actions.click(username_input).send_keys("user")
    actions.perform()
    actions.click(password_input).send_keys("bitnami")
    actions.perform()
    actions.click(browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]'))
    actions.perform()
    wait_element('[id="nav-logout"][class="nav-item"]', browser)

def test_add_item_to_cart(browser):
    browser.get(f"http://{browser.base_url}")
    actions = ActionChains(browser)
    product = browser.find_element(By.CSS_SELECTOR, '[class="product-thumb"]')
    add_to_cart = product.find_element(By.CSS_SELECTOR, 'button[type="submit"][title="Add to Cart"]')
    product_names = product.find_elements(By.CSS_SELECTOR, 'h4 a')
    product_name = product_names[0].text
    actions.click(add_to_cart)
    actions.perform()
    browser.get(f"http://{browser.base_url}/en-gb?route=checkout/cart")
    item_in_cart = browser.find_element(By.CSS_SELECTOR, '[class="text-start text-wrap"] > a')
    assert item_in_cart.text == product_name

def test_change_currency(browser):
    browser.get(f"http://{browser.base_url}")
    old_currency = browser.find_element(By.CSS_SELECTOR, 'strong')
    old_prices = browser.find_elements(By.CSS_SELECTOR, '[class="price-new"]')
    actions = ActionChains(browser)
    currency_dropdown = browser.find_element(By.CSS_SELECTOR, '[id="form-currency"] > div')
    actions.click(currency_dropdown)
    actions.perform()
    currency_list = browser.find_elements(By.CSS_SELECTOR, '[class="dropdown-menu show"] > li > a')
    current_currency = ""
    for currency in currency_list:
        if old_currency.text not in currency.text:
            actions.click(currency)
            current_currency = currency.text
            break
    actions.perform()
    new_prices = browser.find_elements(By.CSS_SELECTOR, '[class="price-new"]')
    for price in new_prices:
        assert price not in old_prices, "New price: {price.text}, with current currency {current_currency}"

def test_currency_in_cart(browser):
    browser.get(f"http://{browser.base_url}")
    actions = ActionChains(browser)

    add_item = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"][title="Add to Cart"]')
    actions.click(add_item)
    actions.click(add_item)
    actions.perform()
    browser.get(f"http://{browser.base_url}/en-gb?route=checkout/cart")
    currency_dropdown = browser.find_element(By.CSS_SELECTOR, '[id="form-currency"] > div')
    actions.click(currency_dropdown)
    actions.perform()
    old_currency = browser.find_element(By.CSS_SELECTOR, 'strong')
    currency_list = browser.find_elements(By.CSS_SELECTOR, '[class="dropdown-menu show"] > li > a')
    old_prices = browser.find_elements(By.XPATH, "//table[@class='table table-bordered']//tbody/tr/td[5][@class='text-end']")
    current_currency = ""
    for currency in currency_list:
        if old_currency.text not in currency.text:
            actions.click(currency)
            current_currency = currency.text
            break
    actions.perform()
    new_prices = browser.find_elements(By.XPATH, "//table[@class='table table-bordered']//tbody/tr/td[5][@class='text-end']")
    for price in new_prices:
        assert price not in old_prices, "New price: {price.text}, with current currency {current_currency}"