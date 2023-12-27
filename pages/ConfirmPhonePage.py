from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure


class ConfirmPhonePageLocators:
    PHONE_FIELD = (By.ID, 'field_phone')
    COUNTRY_LIST_ITEM = (By.XPATH, '//div[@data-l="t,country"]')
    NEXT_BUTTON = (By.XPATH, '//*[@data-l="t,submit"]')
    AGREEMENT_DOC_BUTTON = (By.XPATH, '//*[@data-l="t,agreement"]')
    PRIVACY_DOC_BUTTON = (By.XPATH, '//*[@data-l="t,privacy"]')
    EMPTY_FIELD_ERROR_TEXT = (By.XPATH, '//*[@class="input-e js-ph-vl-hint"]')


class ConfirmPhonePageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.check_page()

    @allure.step('Проверяем наличие элементов на странице "Подтверждения номера"')
    def check_page(self):
        self.find_element(ConfirmPhonePageLocators.PHONE_FIELD)
        self.find_element(ConfirmPhonePageLocators.COUNTRY_LIST_ITEM)
        self.find_element(ConfirmPhonePageLocators.NEXT_BUTTON)
        self.find_element(ConfirmPhonePageLocators.AGREEMENT_DOC_BUTTON)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_next_button(self):
        self.find_element(ConfirmPhonePageLocators.NEXT_BUTTON).click()

    @allure.step('Проверяем текст ошибки при незаполненном поле "Номер телефона"')
    def get_empty_field_error_text(self):
        return self.find_element(ConfirmPhonePageLocators.EMPTY_FIELD_ERROR_TEXT).text
