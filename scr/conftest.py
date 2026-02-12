import allure
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOps
from selenium.webdriver.firefox.options import Options as FFOps

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("log.log")
    ]
)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser = item.funcargs.get("browser")
        if browser:
            screenshot = browser.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=f"Screenshot on failure",
                attachment_type=allure.attachment_type.PNG,
            )


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Default browser is edge, you can also choose chrome or firefox")
    parser.addoption(
        "--url",
        action="store",
        default="192.168.1.110",
        help="This request url"
    )
    parser.addoption(
        "--remote",
        action="store_true",
        help="Run tests on Selenoid"
    )
    parser.addoption(
        "--browser_version",
        default="128.0",
        help="Browser version for remote"
    )
    parser.addoption(
        "--executor",
        default=None,
        help="Executor: selenoid or local"
    )
    parser.addoption(
        "--selenoid_url",
        default="http://localhost:4444/wd/hub",
        help="Selenoid URL"
    )

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    remote = request.config.getoption("--remote")
    browser_version = request.config.getoption("--browser_version")
    executor = request.config.getoption("--executor")
    selenoid_url = request.config.getoption("--selenoid_url")

    driver = None

    if remote or executor == "selenoid":

        if browser_name == "ch":
            options = webdriver.ChromeOptions()
        else:
            options = webdriver.FirefoxOptions()

        options.set_capability("browserName", browser_name if browser_name in ("chrome", "firefox", "edge") else "chrome")
        options.set_capability("browserVersion", browser_version)
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False
        })

        driver = webdriver.Remote(
            command_executor=selenoid_url,
            options=options
        )
    elif browser_name == "chrome":
        options = ChromeOps()
        options.add_argument('--headless=new')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FFOps()
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        from selenium.webdriver.edge.options import Options as EdgeOptions
        options = EdgeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Driver for {browser_name} not supported")

    driver.base_url = base_url
    yield driver
    driver.quit()