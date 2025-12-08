from selenium.webdriver.common.by import By
import time

from .base_page import BasePage
from .objects.cart_page import CartPage
from .objects.register_page import RegisterPage


class MainPage(BasePage):
    PRODUCT_RANDOM = (By.CSS_SELECTOR, '[class="product-thumb"]')
    PRODUCT_ADD_TO_CARD = (By.CSS_SELECTOR, 'button[type="submit"][title="Add to Cart"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'h4 a')
    PRICE_NEW = (By.CSS_SELECTOR, '[class="price-new"]')
    MY_ACCOUNT = (By.XPATH, '//span[text()="My Account"]')
    REGISTER = (By.XPATH, '//a[text()="Register"]')

    def __init__(self, browser):
        url = f"http://{browser.base_url}"
        super().__init__(browser, url)

    def get_random_product(self):
        product = self.find_element(self.PRODUCT_RANDOM)
        return product

    def get_product_name(self, product):
        product_name_element = product.find_element(*self.PRODUCT_NAME)
        return product_name_element.text

    def add_to_cart(self, product):
        add_to_cart_button = product.find_element(*self.PRODUCT_ADD_TO_CARD)
        self.actions.click(add_to_cart_button).perform()
        time.sleep(1)
        return self

    def go_to_cart(self):
        cart_url = f"http://{self.browser.base_url}/en-gb?route=checkout/cart"
        self.browser.get(cart_url)
        time.sleep(1)
        return CartPage(self.browser)

    def get_all_prices(self):
        self.wait_for_element(self.PRICE_NEW)
        price_elements = self.browser.find_elements(*self.PRICE_NEW)
        return [price.text for price in price_elements]

    def open_register(self):
        self.find_element(self.MY_ACCOUNT).click()
        self.wait_for_element(self.REGISTER).click()
        return RegisterPage(self.browser)