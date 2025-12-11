from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from scr.page_objects.base_page import BasePage


class AdminPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[id="input-password"]')
    LOGOUT_LINK = (By.CSS_SELECTOR, '[id="nav-logout"][class="nav-item"]')
    CATALOG = (By.CSS_SELECTOR, '[id="menu-catalog"]')
    PRODUCT = (By.CSS_SELECTOR, '#collapse-1.collapse.show a[href*="route=catalog/product"]')
    ADD_BUTTON = (By.CSS_SELECTOR, '[title="Add New"]')
    DATA_TAB = (By.CSS_SELECTOR, 'a[href="#tab-data"]')
    PRODUCT_NAME_PLACEHOLDER = (By.CSS_SELECTOR, 'input[placeholder="Product Name"]')
    PRODUCT_NAME = "SOME NEW PRODUCT"
    META_TITLE_PLACEHOLDER = (By.CSS_SELECTOR, 'input[placeholder="Meta Tag Title"]')
    MODEL_PLACEHOLDER = (By.CSS_SELECTOR, 'input[placeholder="Model"]')
    SEO_TAB = (By.CSS_SELECTOR, 'a[href="#tab-seo"]')
    KEYWORD_PLACEHOLDER = (By.CSS_SELECTOR, 'input[placeholder="Keyword"]')
    KEYWORD = "222228"
    SUCCESS_DONE = (By.CSS_SELECTOR, '#alert .alert-success')
    RANDOM_ITEM_TO_DELETE = (By.CSS_SELECTOR, 'tbody tr input[name="selected[]"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, '[title="Delete"]')
    def __init__(self, browser):
        url = f"http://{browser.base_url}/administration"
        super().__init__(browser, url)
        self.actions = ActionChains(browser)

    def login(self, username, password):
        self.actions.click(self.find_element(self.USERNAME)).send_keys(username).perform()
        self.actions.click(self.find_element(self.PASSWORD)).send_keys(password).perform()
        self.actions.click(self.find_element(self.SUBMIT)).perform()

    def is_logout_link_visible(self):
        return self.wait_for_element(self.LOGOUT_LINK)

    def open_product_section(self):
        self.actions.click(self.wait_for_element(self.CATALOG)).perform()
        self.actions.click(self.wait_for_element(self.PRODUCT)).perform()

    def open_add_product(self):
        self.actions.click(self.wait_for_element(self.ADD_BUTTON)).perform()

    def fill_required_fields(self):
        self.actions.click(self.wait_for_element(self.PRODUCT_NAME_PLACEHOLDER)).send_keys(self.PRODUCT_NAME).perform()
        self.actions.click(self.wait_for_element(self.META_TITLE_PLACEHOLDER)).send_keys(self.PRODUCT_NAME).perform()
        self.actions.click(self.wait_for_element(self.DATA_TAB)).perform()
        self.actions.click(self.wait_for_element(self.MODEL_PLACEHOLDER)).send_keys(self.PRODUCT_NAME).perform()
        self.actions.click(self.wait_for_element(self.SEO_TAB)).perform()
        self.actions.click(self.wait_for_element(self.KEYWORD_PLACEHOLDER)).send_keys(self.KEYWORD).perform()

    def is_success(self):
        return self.wait_for_element(self.SUCCESS_DONE)

    def delete_some_item(self):
        self.actions.click(self.wait_for_element(self.RANDOM_ITEM_TO_DELETE)).perform()
        self.actions.click(self.wait_for_element(self.DELETE_BUTTON)).perform()
        self.browser.switch_to.alert.accept()