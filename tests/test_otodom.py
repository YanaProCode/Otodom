import pytest
from PO.home import HomePage
from PO.login import LoginPage
import configparser
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from selenium.webdriver.common.by import By

#config = configparser.ConfigParser()
#config.read('config.properties')
#tool = config.get('DEFAULT', 'tool', fallback='playwright')

def test_login_with_correct_creds(page, request):
    tool = request.config.getoption("--tool")
    home_page = HomePage(page, tool)
    login_page = LoginPage(page, tool)
    home_page.navigate()
    home_page.login()
    login_page.fill_login_form('yana.proshack@gmail.com', 'Ya412030')

    if tool == 'playwright':
        assert page.is_visible('//*[@id="__next"]/div[1]/div/div/div[2]/div[1]/a'), 'Login failed'
    elif tool == 'selenium':
        assert page.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div[2]/div[1]/a'), 'Login failed'
