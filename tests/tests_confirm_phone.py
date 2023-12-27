from BaseTest import browser
from BaseTest import open_base_url
from pages.LoginPage import LoginPageHelper
from pages.ConfirmPhonePage import ConfirmPhonePageHelper
import allure

EMPTY_FIELD_ERROR = 'Неправильный номер телефона.'


@allure.suite('Проверка на странице подтверждения номера')
@allure.title('Проверка текста ошибки при пустом поле "Номер телефона"')
def test_empty_phone(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.click_register_button()
    confirm_phone_page_helper = ConfirmPhonePageHelper(browser)
    confirm_phone_page_helper.click_next_button()
    assert confirm_phone_page_helper.get_empty_field_error_text() == EMPTY_FIELD_ERROR
