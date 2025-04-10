import allure
from playwright.sync_api import Page as PlaywrightPage

class LoginPage:

    def __init__(self, page: PlaywrightPage, tool):
        self.page = page
        self.tool = tool
        self.login_header = "//button[@tabindex='-1']"
        self.email_input = "#username"
        self.password_input = "#password"
        self.submit_button = "//button[@type='submit']"
        self.favourites_icon = "//*[@id=\"__next\"]/div[1]/div/div/div[2]/div[1]/a"
        self.favourite_ads_link = "//a[@role='menuitem'][@href='/pl/zapisane/ogloszenia']"
        self.favourite_ads_header = "#link-SAVED_ADS"
        self.error_banner = "#error-banner"
        #self.chats_icon = "//*[@id=\"__next\"]/div[1]/div/div/div[2]/a/svg"
        self.account_icon = "//a[@data-cy='desktop-nav-user-menu.username']"
        self.chats_link = "//li/a[@href='/mojekonto/odpowiedzi']"

    @allure.step("Fill login form")
    def fill_login_form(self, email: str, password: str):
        self.page.wait_for_selector(self.login_header, timeout=10000)
        self.page.wait_for_selector(self.email_input).fill(email)
        self.page.wait_for_selector(self.password_input).fill(password)
        self.page.click(self.submit_button)

    @allure.step("Check successful login")
    def check_successful_login(self):
        self.page.wait_for_selector(self.favourites_icon, timeout=10000)

    @allure.step("Check failed login")
    def check_failed_login(self):
        self.page.wait_for_selector(self.error_banner, timeout=10000)
        assert self.page.is_visible(self.error_banner), "Error message not displayed"

    @allure.step("Open chats")
    def open_chats(self):
        self.page.click(self.account_icon)
        self.page.click(self.chats_link)
        self.page.wait_for_selector("//div[@data-cy='conversationsListColumn']", timeout=10000)
        assert self.page.is_visible("//div[@data-cy='conversationsListColumn']"), "Chats not found"

    @allure.step("Open favourite ads")
    def open_favourite_ads(self):
        self.page.wait_for_selector(self.favourites_icon, timeout=10000)
        self.page.click(self.favourites_icon)
        self.page.wait_for_selector(self.favourite_ads_link, timeout=10000)
        self.page.click(self.favourite_ads_link)
        self.page.wait_for_selector(self.favourite_ads_header)
        assert self.page.is_visible(self.favourite_ads_header), "Favourite ads not found"


