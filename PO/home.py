from playwright.sync_api import Page as PlaywrightPage
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, page: PlaywrightPage, tool):
        self.page = page
        self.tool = tool
        self.login_selector_xpath = "//*[@id=\"__next\"]/div[1]/div/div/div[2]/a/span"
        self.accept_cookies_selector = "#onetrust-accept-btn-handler"

    def navigate(self):
        if self.tool == 'playwright':
            self.page.goto("https://www.otodom.pl/")
            self.accept_cookies()
        elif self.tool == 'selenium':
            self.page.get("https://www.otodom.pl/")
            self.accept_cookies()

    def accept_cookies(self):
        if self.tool == 'playwright':
            if self.page.is_visible(self.accept_cookies_selector):
                self.page.click(self.accept_cookies_selector)

        elif self.tool == 'selenium':
            try:
                WebDriverWait(self.page, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, self.accept_cookies_selector))
                ).click()
            except:
                pass

    def login(self):
        if self.tool == 'playwright':
            self.page.wait_for_selector(self.login_selector_xpath)
            self.page.click(self.login_selector_xpath)


        elif self.tool == 'selenium':
            login_button = WebDriverWait(self.page, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.login_selector_xpath))
            )
            login_button.click()
