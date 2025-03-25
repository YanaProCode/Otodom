from PO.home import HomePage
from PO.login import LoginPage

def test_login_with_correct_creds(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.navigate()
    home_page.login()
    login_page.fill_login_form('yana.proshack@gmail.com', 'Ya412030')
    assert page.is_visible('//*[@id="__next"]/div[1]/div/div/div[2]/div[1]/a'), 'Login failed'

