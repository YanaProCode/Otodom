from playwright.sync_api import Page as PlaywrightPage
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        self.account_icon = "//*[@id=\"__next\"]/div[1]/div/div/div[2]/div[2]/a/div/svg[2]"
        self.chats_link = "//*[@id=\"__next\"]/div[1]/div/div/div[2]/div[2]/ul/li[2]/a"


    def fill_login_form(self, email: str, password: str):
        WebDriverWait(self.page, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.login_header))
        )
        self.page.find_element(By.CSS_SELECTOR, self.email_input).send_keys(email)
        self.page.find_element(By.CSS_SELECTOR, self.password_input).send_keys(password)
        self.page.find_element(By.XPATH, self.submit_button).click()


    def check_successful_login(self):
        WebDriverWait(self.page, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.favourites_button))
        )


    def check_failed_login(self):
        WebDriverWait(self.page, 10).until(
            EC.visibility_of_element_located((By.ID, self.error_banner))
        )

    def open_chats(self):
        self.page.click(self.account_icon)
        self.page.click(self.chats_link)
        WebDriverWait(self.page, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id=\"__next\"]/main/div[2]/div[2]/div/div[1]/h3"))
        )
        #add is_visible


    def open_favourite_ads(self):
        self.page.click(self.favourites_button)
        self.page.click(self.favourite_ads_link)
        WebDriverWait(self.page, 10).until(
            EC.visibility_of_element_located((By.ID, self.favourite_ads_header))
        )
