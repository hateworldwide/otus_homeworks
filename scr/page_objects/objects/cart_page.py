from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from scr.page_objects.base_page import BasePage
from scr.utils.allure_decorators import *


class CartPage(BasePage):
    ITEM_IN_CART = (By.CSS_SELECTOR, '[class="text-start text-wrap"] > a')
    PRICES_IN_CART = (By.XPATH, "//table[@class='table table-bordered']//tbody/tr/td[5][@class='text-end']")
    def __init__(self, browser):
        url = f"http://{browser.base_url}/en-gb?route=checkout/cart"
        super().__init__(browser, url)
        self.actions = ActionChains(browser)

    @allure.step("Get item name")
    @log_action
    @screenshot_on_fail
    def get_item_name(self):
        return self.wait_for_element(self.ITEM_IN_CART).text

    @allure.step("Get all prices")
    @log_action
    @screenshot_on_fail
    def get_all_prices(self):
        self.wait_for_element(self.PRICES_IN_CART)
        price_elements = self.browser.find_elements(*self.PRICES_IN_CART)
        return [price.text for price in price_elements]