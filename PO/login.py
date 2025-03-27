from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.login_header = "//*[@id=\"__next\"]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/header"
        self.email_input = "#username"
        self.password_input = "#password"
        self.submit_button = "//button[@type='submit']"
        self.favourites_button = "//*[@id=\"__next\"]/div[1]/div/div/div[2]/div[1]/a"


    def fill_login_form(self, email: str, password: str):
        self.page.wait_for_selector(self.login_header, timeout=10000)
        self.page.wait_for_selector(self.email_input).fill(email)
        self.page.wait_for_selector(self.password_input).fill(password)
        self.page.click(self.submit_button)
        self.page.wait_for_selector(self.favourites_button, timeout=10000)




