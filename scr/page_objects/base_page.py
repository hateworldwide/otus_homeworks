from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    CURRENT_CURRENCY = (By.CSS_SELECTOR, 'strong')
    PRICE_NEW = (By.CSS_SELECTOR, '[class="price-new"]')
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, '[id="form-currency"] > div')
    CURRENCY_LIST = (By.CSS_SELECTOR, '[class="dropdown-menu show"] > li > a')
    SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"]')
    def __init__(self, browser, base_url=None):
        self.browser = browser
        self.base_url = base_url or getattr(browser, "base_url", "")
        self.wait = WebDriverWait(self.browser, 6)
        self.actions = ActionChains(browser)

    def open(self, url=None):
        url_to_open = url or self.base_url
        if url_to_open:
            self.browser.get(url_to_open)
        else:
            raise ValueError("URL не указан для открытия страницы")
        return self

    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def wait_for_element(self, selector: tuple):
        try:
            return WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutException:
            raise AssertionError("Cant find elements by locator: {}".format(selector))


    def get_current_currency(self):
        return self.find_element(self.CURRENT_CURRENCY).text


    def open_currency_dropdown(self):
        currency_dropdown = self.browser.find_element(*self.CURRENCY_DROPDOWN)
        self.actions.click(currency_dropdown).perform()
        return self

    def switch_to_different_currency(self):
        current_currency = self.get_current_currency()
        self.open_currency_dropdown()
        currency_options = self.browser.find_elements(*self.CURRENCY_LIST)
        for currency_option in currency_options:
            if current_currency not in currency_option.text:
                self.actions.click(currency_option).perform()
                return currency_option.text
        return None

    def check_currencies(self, old_currency, new_currency):
        assert old_currency != new_currency, f"Валюта не изменилась. Текущая валюта: {old_currency}"

    def check_prices(self, new_currency, prices: enumerate):
        for i, (old_price, new_price) in prices:
            assert old_price != new_price, (
                f"Цена не изменилась после смены валюты.\n"
                f"Старая цена: {old_price}\n"
                f"Новая цена: {new_price}\n"
                f"Текущая валюта: {new_currency}"
            )

    def submit(self):
        self.actions.click(self.find_element(self.SUBMIT)).perform()