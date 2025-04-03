from playwright.sync_api import Page as PlaywrightPage

class LoginPage:

    def __init__(self, page: PlaywrightPage, tool):
        self.page = page
        self.tool = tool
        self.login_header = "//*[@id=\"__next\"]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/header"
        self.email_input = "#username"
        self.password_input = "#password"
        self.submit_button = "//button[@type='submit']"
        self.favourites_button = "//*[@id=\"__next\"]/div[1]/div/div/div[2]/div[1]/a"
        self.favourite_ads_link = "//*[@id=\"__next\"]/div[1]/div/div/div[2]/div[1]/ul/li[1]/a"
        self.favourite_ads_header = "#link-SAVED_ADS"
        self.error_banner = "#error-banner"
        self.chats_icon = "//*[@id=\"__next\"]/div[1]/div/div/div[2]/a/svg"
        self.account_icon = "//a[@data-cy='desktop-nav-user-menu.username']"
        self.chats_link = "//li/a[@href='/mojekonto/odpowiedzi']"


    def fill_login_form(self, email: str, password: str):
        self.page.wait_for_selector(self.login_header, timeout=10000)
        self.page.wait_for_selector(self.email_input).fill(email)
        self.page.wait_for_selector(self.password_input).fill(password)
        self.page.click(self.submit_button)

    def check_successful_login(self):
        self.page.wait_for_selector(self.favourites_button, timeout=10000)


    def check_failed_login(self):
        self.page.wait_for_selector(self.error_banner, timeout=10000)


    def open_chats(self):
        self.page.click(self.account_icon)
        self.page.click(self.chats_link)
        self.page.wait_for_selector("//*[@id=\"__next\"]/main/div[2]/div[2]/div/div[1]/h3", timeout=10000)
            #add is_visible


    def open_favourite_ads(self):
        self.page.click(self.favourites_button)
        self.page.click(self.favourite_ads_link)
        self.page.wait_for_selector(self.favourite_ads_header)

