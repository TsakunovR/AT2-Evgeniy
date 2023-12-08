from BaseTest import browser
from BaseTest import open_base_url
from pages.LoginPage import LoginPageHelper
import allure

EMPTY_FORM_ERROR = 'Введите логин'
EMPTY_PASSWORD_ERROR = 'Введите пароль'
INCORRECT_PASSWORD_ERROR = 'Неправильно указан логин и/или пароль'
LOGIN = 'Иван'
PASSWORD = '12345'


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки на пустые поля "Логин/Пароль" в форме авторизации')
def test_empty_auth_form(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.click_login_button()
    assert login_page_helper.get_error_text() == EMPTY_FORM_ERROR


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки на пустое поле "Пароль" в форме авторизации')
def test_empty_password(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.set_login(LOGIN)
    login_page_helper.click_login_button()
    assert login_page_helper.get_error_text() == EMPTY_PASSWORD_ERROR


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при вводе некорректного логина/пароля')
def test_incorrect_password(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.set_login(LOGIN)
    login_page_helper.set_password(PASSWORD)
    login_page_helper.click_login_button()
    assert login_page_helper.get_error_text() == INCORRECT_PASSWORD_ERROR
