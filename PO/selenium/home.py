import allure
from playwright.sync_api import Page as PlaywrightPage
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, page: PlaywrightPage, tool):
        self.page = page
        self.tool = tool
        self.login_selector_xpath = "//div/a[@data-cy='navbar-my-account-button']"
        self.accept_cookies_selector = "#onetrust-accept-btn-handler"

    @allure.step("Navigate")
    def navigate(self):
        self.page.get("https://www.otodom.pl/")
        self.accept_cookies()

    @allure.step("Accept cookies")
    def accept_cookies(self):
        try:
            WebDriverWait(self.page, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.accept_cookies_selector))
            ).click()
        except:
            pass

    @allure.step("Login")
    def login(self):
        login_button = WebDriverWait(self.page, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_selector_xpath))
        )
        login_button.click()
