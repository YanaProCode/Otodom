import allure
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    ACCOUNT_ADS_LINK = "//div/div[@role='navigation']/a[@data-cy='desktop-nav-user-menu.username']"
    FAVOURITES_ADS_LINK = "//div/div[@role='navigation']/a[not(@data-cy='desktop-nav-user-menu.username')]"

    NEWS = "//ul[@role='menu']/li/a[@role='menuitem'][2]"

    def __init__(self, page: SeleniumWebDriver, tool):
        self.page = page
        self.tool = tool
        self.login_header = "//button[@tabindex='-1']"
        self.email_input = "#username"
        self.password_input = "#password"
        self.submit_button = "//button[@type='submit']"
        self.favourites_icon = "//*[@id=\"__next\"]/div[1]/div/div/div[2]/div[1]/a"
        self.favourite_ads_link = "//a[@role='menuitem'][@href='/pl/zapisane/ogloszenia']"
        self.favourite_ads_header = "link-SAVED_ADS"
        self.error_banner = "error-banner"
        #self.chats_icon = "//*[@id=\"__next\"]/div[1]/div/div/div[2]/a/svg"
        self.account_icon = "//a[@data-cy='desktop-nav-user-menu.username']"
        self.chats_link = "//li/a[@href='/mojekonto/odpowiedzi']"

    @allure.step("Fill login form")
    def fill_login_form(self, email: str, password: str):
        WebDriverWait(self.page, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.login_header))
        )
        self.page.find_element(By.CSS_SELECTOR, self.email_input).send_keys(email)
        self.page.find_element(By.CSS_SELECTOR, self.password_input).send_keys(password)
        self.page.find_element(By.XPATH, self.submit_button).click()

    @allure.step("Check successful login")
    def check_successful_login(self):
        WebDriverWait(self.page, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.favourites_icon))
        )

    @allure.step("Check failed login")
    def check_failed_login(self):
        WebDriverWait(self.page, 10).until(
            EC.visibility_of_element_located((By.ID, self.error_banner))
        )
        assert self.page.find_element(By.ID,
                                      self.error_banner).is_displayed(), "Error message not displayed"

    @allure.step("Open chats")
    def open_chats(self):
        self.page.find_element(By.XPATH, self.ACCOUNT_ADS_LINK).click()
        self.page.find_element(By.XPATH, self.NEWS).click()
        WebDriverWait(self.page, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@data-cy='conversationsListColumn']"))
        )
        assert self.page.find_element(By.XPATH,
                                      "//div[@data-cy='conversationsListColumn']").is_displayed(), "Chats not found"

    @allure.step("Open favourite ads")
    def open_favourite_ads(self):
        self.page.find_element(By.XPATH, self.favourites_icon).click()
        WebDriverWait(self.page, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.favourite_ads_link))
        )
        self.page.find_element(By.XPATH, self.favourite_ads_link).click()
        WebDriverWait(self.page, 10).until(
            EC.visibility_of_element_located((By.ID, self.favourite_ads_header))
        )
        assert self.page.find_element(By.ID, self.favourite_ads_header).is_displayed(), "Favourite ads not found"
