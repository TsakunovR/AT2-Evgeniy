from BaseTest import browser
from BaseTest import open_base_url
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper
from pages.RecoveryByPhonePage import RecoveryByPhonePageHelper
from pages.RecoveryByEmailPage import RecoveryByEmailPageHelper
import allure

LOGIN = 'Иван'
PASSWORD = '12345'
TITLE_TEXT = 'Восстановление доступа'
URL = 'https://ok.ru/dk?st.cmd=anonymRecoveryStart'
EMPTY_FIELD_ERROR = 'Неправильный формат почты'


@allure.suite('Форма авторизации')
@allure.title('Переход на страницу восстановления профиля')
def test_go_to_recovery_page(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.set_login(LOGIN)
    for i in range(3):
        login_page_helper.set_password(PASSWORD)
        login_page_helper.click_login_button()
    recovery_page_helper = RecoveryPageHelper(browser)
    recovery_page_helper.click_recovery_button()
    base_page = BasePage(browser)
    assert base_page.get_url() == URL


@allure.suite('Восстановление профиля')
@allure.title(
    'Восстановление профиля по номеру телефона. Проверка соответствия маски коду страны в поле "Номер телефона"')
def test_recovery_by_phone(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.click_recovery_button()
    recovery_page_helper = RecoveryPageHelper(browser)
    recovery_page_helper.click_phone_button()
    recovery_by_phone_page = RecoveryByPhonePageHelper(browser)
    country_code = recovery_by_phone_page.select_country(2)
    assert country_code == recovery_by_phone_page.get_value()


@allure.title('Восстановление профиля по email. Проверка ошибки на пустое поле "email"')
def test_recovery_by_email(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.click_recovery_button()
    recovery_page_helper = RecoveryPageHelper(browser)
    recovery_page_helper.click_email_button()
    recovery_by_email_page = RecoveryByEmailPageHelper(browser)
    recovery_by_email_page.click_get_code_button()
    assert recovery_by_email_page.get_empty_field_error_text() == EMPTY_FIELD_ERROR
