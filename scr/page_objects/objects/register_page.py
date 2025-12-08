import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from scr.page_objects.base_page import BasePage


class RegisterPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, 'input[name="firstname"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[name="lastname"]')
    EMAIL = (By.CSS_SELECTOR, 'input[name="email"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
    AGREE = (By.CSS_SELECTOR, 'input[name="agree"]')
    SUCCESS = (By.CSS_SELECTOR, '#content h1')

    def __init__(self, browser):
        url = f"http://{browser.base_url}/en-gb?route=account/register"
        super().__init__(browser, url)
        self.actions = ActionChains(browser)

    def fill_fields(self):
        self.actions.click(self.wait_for_element(self.FIRST_NAME)).send_keys("John").perform()
        self.actions.click(self.find_element(self.LAST_NAME)).send_keys("John").perform()
        self.actions.click(self.find_element(self.EMAIL)).send_keys("John121114@yaya.ru").perform()
        self.actions.click(self.find_element(self.PASSWORD)).send_keys("John").perform()
        self.actions.click(self.find_element(self.AGREE)).perform()

    def is_success(self):
        time.sleep(1)
        status = self.wait_for_element(self.SUCCESS).text
        assert status == "Your Account Has Been Created!"