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
        if self.tool == "playwright":
            self.page.wait_for_selector(self.login_header, timeout=10000)
            self.page.wait_for_selector(self.email_input).fill(email)
            self.page.wait_for_selector(self.password_input).fill(password)
            self.page.click(self.submit_button)
        elif self.tool == "selenium":
            WebDriverWait(self.page, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.login_header))
            )
            self.page.find_element(By.CSS_SELECTOR, self.email_input).send_keys(email)
            self.page.find_element(By.CSS_SELECTOR, self.password_input).send_keys(password)
            self.page.find_element(By.XPATH, self.submit_button).click()
    def check_successful_login(self):
        if self.tool == 'playwright':
            self.page.wait_for_selector(self.favourites_button, timeout=10000)
        elif self.tool == 'selenium':
            WebDriverWait(self.page, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.favourites_button))
            )

    def check_failed_login(self):
        if self.tool == 'playwright':
            self.page.wait_for_selector(self.error_banner, timeout=10000)
        elif self.tool == 'selenium':
            WebDriverWait(self.page, 10).until(
                EC.visibility_of_element_located((By.ID, self.error_banner))
            )

    def open_chats(self):
        if self.tool == 'playwright':
            self.page.click(self.account_icon)
            self.page.click(self.chats_link)
            self.page.wait_for_selector("//*[@id=\"__next\"]/main/div[2]/div[2]/div/div[1]/h3", timeout=10000)
        elif self.tool == 'selenium':
            self.page.click(self.account_icon)
            self.page.click(self.chats_link)
            WebDriverWait(self.page, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id=\"__next\"]/main/div[2]/div[2]/div/div[1]/h3"))
            )

    def open_favourite_ads(self):
        if self.tool == "playwright":
            self.page.click(self.favourites_button)
            self.page.click(self.favourite_ads_link)
            self.page.wait_for_selector(self.favourite_ads_header)
        elif self.tool == "selenium":
            self.page.click(self.favourites_button)
            self.page.click(self.favourite_ads_link)
            WebDriverWait(self.page, 10).until(
                EC.visibility_of_element_located((By.ID, self.favourite_ads_header))
            )
