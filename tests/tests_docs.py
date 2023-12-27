from BaseTest import browser
from BaseTest import open_base_url
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.DocsPage import DocsPageHelper
import allure

URL = 'https://ok.ru/agreementpage'


@allure.suite('Проверка формы авторизации')
@allure.title('Переход на страницу "Соглашения и политики"')
def test_go_to_docs_page(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.click_agreement_button()
    DocsPageHelper(browser)
    assert BasePage(browser).get_url() == URL
