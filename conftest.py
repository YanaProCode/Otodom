import pytest
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.service import Service as SafariService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chromium", help="Browser to run tests with: chromium, firefox, or webkit"
    )
    parser.addoption(
        "--tool", action="store", default="playwright", help="Tool to run tests with: playwright or selenium"
    )

@pytest.fixture(scope="function")
def page(request):
    tool = request.config.getoption("--tool")
    browser_type = request.config.getoption("--browser")

    if tool == 'playwright':
        with sync_playwright() as p:
            browser = getattr(p, browser_type).launch(headless=False, slow_mo=500)
            context = browser.new_context()
            page = context.new_page()
            #stealth_sync(page)
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


