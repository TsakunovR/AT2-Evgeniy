from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure


class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_INPUT = (By.ID, 'field_email')
    PASSWORD_INPUT = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    RECOVERY_BUTTON = (By.XPATH, '//a[@data-l="t,restore"]')
    REGISTER_BUTT0N = (By.XPATH, '//*[@data-l="t,register"]')
    VK_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAILRU_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    GOOGLE_BUTTON = (By.XPATH, '//*[@data-l="t,google"]')
    YANDEX_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    APPLE_BUTTON = (By.XPATH, '//*[@data-l="t,apple"]')
    ERROR_FIELD = (By.XPATH, '//div[@class="input-e login_error"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.check_page()

    @allure.step('Проверяем наличие элементов в форме авторизации')
    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_INPUT)
        self.find_element(LoginPageLocators.PASSWORD_INPUT)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.QR_BUTTON)
        self.find_element(LoginPageLocators.RECOVERY_BUTTON)
        self.find_element(LoginPageLocators.REGISTER_BUTT0N)
        self.find_element(LoginPageLocators.VK_BUTTON)
        self.find_element(LoginPageLocators.MAILRU_BUTTON)
        self.find_element(LoginPageLocators.GOOGLE_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_BUTTON)
        self.find_element(LoginPageLocators.APPLE_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)

    @allure.step('Вводим значение в поле "Логин"')
    def set_login(self, login):
        return self.find_element(LoginPageLocators.LOGIN_INPUT).send_keys(login)

    @allure.step('Вводим значение в поле "Пароль"')
    def set_password(self, password):
        return self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step('Кликаем на кнопку "Войти в одноклассники"')
    def click_login_button(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Проверяем текст ошибки')
    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_FIELD).text
