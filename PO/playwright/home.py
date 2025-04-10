import allure
from playwright.sync_api import Page as PlaywrightPage


class HomePage:

    def __init__(self, page: PlaywrightPage, tool):
        self.page = page
        self.tool = tool
        self.login_selector_xpath = "//div/a[@data-cy='navbar-my-account-button']"
        self.accept_cookies_selector = "#onetrust-accept-btn-handler"

    @allure.step("Navigate")
    def navigate(self):
        self.page.goto("https://www.otodom.pl/")
        self.accept_cookies()

    @allure.step("Accept cookies")
    def accept_cookies(self):
        if self.page.is_visible(self.accept_cookies_selector):
            self.page.click(self.accept_cookies_selector)

    @allure.step("Login")
    def login(self):
        self.page.wait_for_selector(self.login_selector_xpath)
        self.page.click(self.login_selector_xpath)

