from PO.home import HomePage
from playwright.sync_api import sync_playwright

def test_login_with_correct_creds():
    with (sync_playwright() as p):
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        home_page = HomePage(page)
        home_page.navigate().login().fill_login_form('yana.proshack@gmail.com', 'Ya412030')
        assert page.is_visible('//*[@id="__next"]/div[1]/div/div/div[2]/div[1]/a'), 'Login failed'

        page.close()
        context.close()
        browser.close()