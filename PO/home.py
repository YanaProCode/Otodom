from playwright.sync_api import Page

class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.login_selector_xpath = "//*[@id=\"__next\"]/div[1]/div/div/div[2]/a/span"
        self.accept_cookies_selector = "#onetrust-accept-btn-handler"

    def navigate(self):
        self.page.goto("https://www.otodom.pl/")
        self.accept_cookies()

    def accept_cookies(self):
        if self.page.is_visible(self.accept_cookies_selector):
            self.page.click(self.accept_cookies_selector)

    def login(self):
        self.page.wait_for_selector(self.login_selector_xpath)
        self.page.click(self.login_selector_xpath)

