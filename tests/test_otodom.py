from PO.playwright.home import HomePage
from PO.playwright.login import LoginPage
from selenium.webdriver.common.by import By


def test_login_with_correct_creds(page, page_objects, request):
    tool = request.config.getoption("--test-tool")
    HomePage, LoginPage = page_objects

    home_page = HomePage(page, tool)
    login_page = LoginPage(page, tool)
    home_page.navigate()
    home_page.login()
    login_page.fill_login_form('yana.proshack@gmail.com', 'Ya412030')
    login_page.check_successful_login()

    if tool == 'playwright':
        assert page.is_visible('//*[@id="__next"]/div[1]/div/div/div[2]/div[1]/a'), 'Login failed'
    elif tool == 'selenium':
        assert page.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div[2]/div[1]/a'), 'Login failed'

def test_login_with_incorrect_creds(page, page_objects, request):
    tool = request.config.getoption("--test-tool")
    HomePage, LoginPage = page_objects

    home_page = HomePage(page, tool)
    login_page = LoginPage(page, tool)
    home_page.navigate()
    home_page.login()
    login_page.fill_login_form('invalid.email@example.com', 'wrongpassword')
    login_page.check_failed_login()


def test_open_chats(page, page_objects, request):
    tool = request.config.getoption("--test-tool")
    HomePage, LoginPage = page_objects

    home_page = HomePage(page, tool)
    login_page = LoginPage(page, tool)
    home_page.navigate()
    home_page.login()
    login_page.fill_login_form('yana.proshack@gmail.com', 'Ya412030')
    login_page.check_successful_login()
    login_page.open_chats()


def test_open_favourite_ads(page, page_objects, request):
    tool = request.config.getoption("--test-tool")
    HomePage, LoginPage = page_objects

    home_page = HomePage(page, tool)
    login_page = LoginPage(page, tool)
    home_page.navigate()
    home_page.login()
    login_page.fill_login_form('yana.proshack@gmail.com', 'Ya412030')
    login_page.check_successful_login()
    login_page.open_favourite_ads()
