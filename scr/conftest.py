import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOps
from selenium.webdriver.firefox.options import Options as FFOps

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Default browser is edge, you can also choose chrome or firefox")
    parser.addoption(
        "--url",
        action="store",
        default="localhost",
        help="This request url"
    )

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")

    if browser_name == "chrome":
        options = ChromeOps()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FFOps()
        driver = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        from selenium.webdriver.edge.options import Options as EdgeOptions
        options = EdgeOptions()
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Driver for {browser_name} not supported")

    driver.base_url = base_url

    yield driver

    driver.quit()