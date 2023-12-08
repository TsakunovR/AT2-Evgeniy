from BaseTest import browser
from BaseTest import open_base_url
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper
import allure

LOGIN = 'Иван'
PASSWORD = '12345'
TITLE_TEXT = 'Восстановление доступа'
URL = 'https://ok.ru/dk?st.cmd=anonymRecoveryStart'


@allure.suite('Проверка формы авторизации')
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
