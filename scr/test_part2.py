from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from scr.conftest import browser

def wait_element(selector, driver, timeout=1, by=By.CSS_SELECTOR):
    try:
        return WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((by, selector)))
    except TimeoutException:
        driver.save_screenshot("{}.png".format(driver.session_id))
        raise AssertionError("Не дождался видимости элемента: {}".format(selector))

def test_main_page(browser):
    browser.get(f"http://{browser.base_url}/")
    wait_element('[class="product-thumb"] > div', browser)
    assert browser.find_element(value="menu"), "No menu on page"
    assert browser.find_element(By.CSS_SELECTOR, 'input[name="search"][placeholder="Search"]'), "No search panel"

    cart_button_text = browser.find_element(By.CSS_SELECTOR, 'button[data-bs-toggle="dropdown"]')
    assert cart_button_text.text == "0 item(s) - $0.00", "Some items in card"

    menu_panel_list = browser.find_elements(By.CSS_SELECTOR, 'ul[class="nav navbar-nav"] > li')
    assert len(menu_panel_list) == 8, "Wrong count of buttons on menu panel: {len(menu_panel_list)}"

    featured_panel_list = browser.find_elements(By.CSS_SELECTOR, '[class="col mb-3"]')
    assert len(featured_panel_list) == 4, "Wrong count of buttons on featured page: {len(featured_panel_list)}"

def test_catalog_page(browser):
    browser.get(f"http://{browser.base_url}/en-gb/catalog/desktops")

    wait_element('[id="compare-total"]', browser)
    sort_by_list = browser.find_elements(By.CSS_SELECTOR, 'select[id="input-sort"] > option')
    assert len(sort_by_list) == 9, "Wrong count of options in sort list: {len(sort_by_list)}"

    limit_list = browser.find_elements(By.CSS_SELECTOR, 'select[id="input-limit"] > option')
    assert len(limit_list) == 5, "Wrong count of options in limit list: {len(limit_list)}"

    product_list = browser.find_elements(By.CSS_SELECTOR, '[class="product-thumb"]')
    limit = browser.find_element(By.CSS_SELECTOR, 'select[id="input-limit"] > option[selected]')
    assert len(product_list) <= int(limit.text), "Count of products on page ({len(product_list)}) more than limit ({limit.text})"

    assert browser.find_element(By.XPATH, '//form[@id="form-currency"]//a[text()="€ Euro"]'), "No euro in currency list"

    cart = browser.find_element(By.CSS_SELECTOR, 'a[title="Shopping Cart"]')
    assert cart.get_attribute('href') == f"http://{browser.base_url}/en-gb?route=checkout/cart", "Wrong cart url: {cart.get_attribute('href')}"

def test_product_page(browser):
    browser.get(f"http://{browser.base_url}/en-gb/product/canon-eos-5d")
    wait_element('[class="price-new"]', browser)

    assert browser.find_element(By.CSS_SELECTOR, 'button[title="Add to Wish List"]'), "No button: add to wish list"

    compare_button = browser.find_element(By.CSS_SELECTOR, 'button[title="Compare this Product"]')
    assert compare_button.get_attribute('formaction') == f"http://{browser.base_url}/en-gb?route=product/compare.add", "Wrong compare button url: {compare_button.get_attribute('formaction')}"

    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, 'button[id="button-cart"]')
    assert add_to_cart_button.text == "Add to Cart", "Wrong text in add_to_cart_button: {add_to_cart_button.text}"

    my_account = browser.find_element(By.XPATH, '//a[text()="My Account"]')
    assert my_account.get_attribute('href') == f"http://{browser.base_url}/en-gb?route=account/account", "Wrong account url: {my_account.get_attribute('href')}"

    contact_us = browser.find_element(By.XPATH, '//a[text()="Contact Us"]')
    assert contact_us.get_attribute('href') == f"http://{browser.base_url}/en-gb?route=information/contact", "Wrong contact url: {contact_us.get_attribute('href')}"

def test_admin_form(browser):
    browser.get(f"http://{browser.base_url}/administration")
    wait_element('[id="form-login"]', browser)

    card_header = browser.find_element(By.CSS_SELECTOR, '[class="card-header"]')
    assert card_header.text == "Please enter your login details.", "Wrong cart header text: {card_header.text}"

    username_header = browser.find_element(By.CSS_SELECTOR, 'label[for="input-username"]')
    assert username_header.text == "Username"

    assert browser.find_element(By.CSS_SELECTOR, 'input[id = "input-username"]'), "No input for username"
    assert browser.find_element(By.CSS_SELECTOR, 'input[id = "input-password"]'), "No input for password"

    login_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    assert login_button.text == "Login", "Wrong login button: {login_button.text}"

def test_registration_form(browser):
    browser.get(f"http://{browser.base_url}/en-gb?route=account/register")
    wait_element('label[for="input-password"]', browser)
    assert browser.find_element(By.XPATH, '//h1[text()="Register Account"]'), "No main header"
    assert browser.find_element(By.CSS_SELECTOR, 'input[id="input-email"]'), "No input for email"
    assert browser.find_element(By.CSS_SELECTOR, 'input[id = "input-password"]'), "No input for password"
    assert browser.find_element(By.CSS_SELECTOR, 'input[type = "checkbox"][id="input-newsletter"]'), "No checkbox for newsletter"
    assert browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]'), "No continue button"
