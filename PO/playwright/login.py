import allure
from playwright.sync_api import Page as PlaywrightPage

class LoginPage:

    LOGIN_BTN = "//div[@data-testid='tabs']//button[1]"
    REGISTRATION_BTN = "//div[@data-testid='tabs']//button[2]"
    SUBMIT_BTN = "//button[@type='submit']"
    ACCOUNT_ADS_LINK = "//div/div[@role='navigation']/a[@data-cy='desktop-nav-user-menu.username']"
    FAVOURITES_ADS_LINK = "//div/div[@role='navigation']/a[not(@data-cy='desktop-nav-user-menu.username')]"
    CONVERSATION_COL = "//div[@data-cy='conversationsListColumn']"

    NOTIFICATIONS = "//ul[@role='menu']/li[1]/a[@role='menuitem']"
    NEWS = "//ul[@role='menu']/li[2]/a[@role='menuitem']"

    def __init__(self, page: PlaywrightPage, tool):
        self.page = page
        self.tool = tool
        self.email_input = "#username"
        self.password_input = "#password"
        self.submit_button = "//button[@type='submit']"
        self.favourite_ads_header = "#link-SAVED_ADS"
        self.error_banner = "#error-banner"
        #self.chats_icon = "//*[@id=\"__next\"]/div[1]/div/div/div[2]/a/svg"
        self.chats_link = "//li/a[@href='/mojekonto/odpowiedzi']"

    @allure.step("Fill login form")
    def fill_login_form(self, email: str, password: str):
        self.page.wait_for_selector(self.LOGIN_BTN, timeout=10000)
        self.page.wait_for_selector(self.email_input).fill(email)
        self.page.wait_for_selector(self.password_input).fill(password)
        self.page.click(self.SUBMIT_BTN)

    @allure.step("Check successful login")
    def check_successful_login(self):
        self.page.wait_for_load_state("load")
        self.page.wait_for_selector(self.FAVOURITES_ADS_LINK, timeout=10000)

    @allure.step("Check failed login")
    def check_failed_login(self):
        self.page.wait_for_selector(self.error_banner, timeout=10000)
        assert self.page.is_visible(self.error_banner), "Error message not displayed"

    @allure.step("Open chats")
    def open_chats(self):
        self.page.wait_for_selector(self.ACCOUNT_ADS_LINK).click()
        self.page.wait_for_selector(self.NEWS).click()
        assert self.page.wait_for_selector(self.CONVERSATION_COL, timeout=10000).is_visible(), "Chats not found"

    @allure.step("Open favourite ads")
    def open_favourite_ads(self):
        self.page.wait_for_selector(self.FAVOURITES_ADS_LINK, timeout=10000).click()
        assert self.page.wait_for_selector(self.favourite_ads_header).page.is_visible(self.favourite_ads_header), "Favourite ads not found"


