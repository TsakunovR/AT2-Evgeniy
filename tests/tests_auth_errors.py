from BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper

URL = "https://ok.ru"
EMPTY_FORM_ERROR = "Введите логин"
EMPTY_PASSWORD_ERROR = "Введите пароль"
INCORRECT_PASSWORD_ERROR = "Неправильно указан логин и/или пароль"
LOGIN = "Иван"
PASSWORD = "12345"


def test_empty_auth_form(browser):
    base_page = BasePage(browser)
    base_page.go_to_url(URL)
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.click_login_button()
    assert login_page_helper.get_error_text() == EMPTY_FORM_ERROR


def test_empty_password(browser):
    base_page = BasePage(browser)
    base_page.go_to_url(URL)
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.set_login(LOGIN)
    login_page_helper.click_login_button()
    assert login_page_helper.get_error_text() == EMPTY_PASSWORD_ERROR


def test_incorrect_password(browser):
    base_page = BasePage(browser)
    base_page.go_to_url(URL)
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.set_login(LOGIN)
    login_page_helper.set_password(PASSWORD)
    login_page_helper.click_login_button()
    assert login_page_helper.get_error_text() == INCORRECT_PASSWORD_ERROR
