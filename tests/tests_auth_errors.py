from BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper

URL = "https://ok.ru"

def test_empty_auth_form(browser):
        base_page = BasePage(browser)
        base_page.go_to_url(URL)
        LoginPageHelper(browser)