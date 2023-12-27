from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure


class RecoveryByEmailPageLocators:
    EMAIL_FIELD = (By.ID, 'field_email')
    GET_CODE_BUTTON = (By.XPATH, '//*[@data-l="t,submit"]')
    EMPTY_FIELD_ERROR_TEXT = (By.XPATH, '//div[@class="input-e"]')


class RecoveryByEmailPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.check_page()

    @allure.step('Проверяем наличие элементов на странице')
    def check_page(self):
        self.find_element(RecoveryByEmailPageLocators.EMAIL_FIELD)
        self.find_element(RecoveryByEmailPageLocators.GET_CODE_BUTTON)

    @allure.step('Кликаем на кнопку "Получить код"')
    def click_get_code_button(self):
        self.find_element(RecoveryByEmailPageLocators.GET_CODE_BUTTON).click()

    @allure.step('Проверяем текст ошибки при незаполненном поле "Email"')
    def get_empty_field_error_text(self):
        return self.find_element(RecoveryByEmailPageLocators.EMPTY_FIELD_ERROR_TEXT).text
