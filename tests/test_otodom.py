import pytest
from PO.home import HomePage
from PO.login import LoginPage
import configparser
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from selenium.webdriver.common.by import By


def test_login_with_correct_creds(page, request):
    tool = request.config.getoption("--tool")
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

def test_login_with_incorrect_creds(page, request):
    tool = request.config.getoption("--tool")
    home_page = HomePage(page, tool)
    login_page = LoginPage(page, tool)
    home_page.navigate()
    home_page.login()
    login_page.fill_login_form('invalid.email@example.com', 'wrongpassword')
    login_page.check_failed_login()

    if tool == 'playwright':
        assert page.is_visible('#error-banner'), 'Error message not displayed'
    elif tool == 'selenium':
        assert page.find_element(By.ID, '#error-banner'), 'Error message not displayed'

def test_open_chats(page, request):
    tool = request.config.getoption("--tool")
    home_page = HomePage(page, tool)
    login_page = LoginPage(page, tool)
    home_page.navigate()
    home_page.login()
    login_page.fill_login_form('yana.proshack@gmail.com', 'Ya412030')
    login_page.check_successful_login()
    login_page.open_chats()

    if tool == 'playwright':
        assert page.is_visible("//*[@id=\"__next\"]/main/div[2]/div[2]/div/div[1]/h3"), 'Chats not found'
    elif tool == 'selenium':
        assert page.find_element(By.XPATH, "//*[@id=\"__next\"]/main/div[2]/div[2]/div/div[1]/h3"), 'Chats not found'

def test_open_favourite_ads(page, request):
    tool = request.config.getoption("--tool")
    home_page = HomePage(page, tool)
    login_page = LoginPage(page, tool)
    home_page.navigate()
    home_page.login()
    login_page.fill_login_form('yana.proshack@gmail.com', 'Ya412030')
    login_page.check_successful_login()
    login_page.open_favourite_ads()

    if tool == 'playwright':
        assert page.is_visible("#link-SAVED_ADS"), 'Ads not found'
    elif tool == 'selenium':
        assert page.find_element(By.ID, "#link-SAVED_ADS"), 'Ads not found'
