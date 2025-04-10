import allure
import pytest
import importlib
from playwright.sync_api import sync_playwright
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.service import Service as SafariService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--test-browser", action="store", default="chromium",
        help="Browser to run tests with: chromium, firefox, or webkit"
    )
    parser.addoption(
        "--test-tool", action="store", default="playwright",
        help="Tool to run tests with: playwright or selenium"
    )

@pytest.fixture(scope="function")
def page(request):
    tool = request.config.getoption("--test-tool")
    browser_type = request.config.getoption("--test-browser")

    if tool == 'playwright':
        with sync_playwright() as p:
            browser = getattr(p, browser_type).launch(headless=False, slow_mo=500)
            context = browser.new_context(
                viewport={"width": 1920, "height": 1080}
            )
            page = context.new_page()
            yield page
            browser.close()

    elif tool == 'selenium':
        if browser_type == 'chromium':
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser_type == 'firefox':
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser_type == 'webkit':
            driver = webdriver.Safari(service=SafariService())
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")
        driver.maximize_window()

        yield driver
        driver.quit()
    else:
        raise ValueError(f"Unsupported tool: {tool}")


@pytest.fixture(scope="function")
def page_objects(request):
    tool = request.config.getoption("--test-tool")

    if tool == 'playwright':
        HomePage = importlib.import_module('PO.playwright.home').HomePage
        LoginPage = importlib.import_module('PO.playwright.login').LoginPage
    elif tool == 'selenium':
        HomePage = importlib.import_module('PO.selenium.home').HomePage
        LoginPage = importlib.import_module('PO.selenium.login').LoginPage
    else:
        raise ValueError(f"Unsupported tool: {tool}")

    return HomePage, LoginPage

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        page = item.funcargs.get('page')
        if page:
            screenshot = page.screenshot()
            allure.attach(screenshot, name="error_screenshot", attachment_type=allure.attachment_type.PNG)
