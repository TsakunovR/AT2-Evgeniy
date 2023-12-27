from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure


class RecoveryPageLocators:
    RECOVERY_PROFILE_BUTTON = (By.XPATH, '//button[@data-l="t,restore"]')
    PHONE_BUTTON = (By.XPATH, '//*[@data-l="t,phone"]')
    EMAIL_BUTTON = (By.XPATH, '//*[@data-l="t,email"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="support-link_item-text"]')


class RecoveryPageHelper(BasePage):

    @allure.step('Проверяем наличие элементов в форме авторизации')
    def check_page(self):
        self.find_element(RecoveryPageLocators.RECOVERY_PROFILE_BUTTON)
        self.find_element(RecoveryPageLocators.PHONE_BUTTON)
        self.find_element(RecoveryPageLocators.EMAIL_BUTTON)


    @allure.step('Кликаем на кнопку "Восстановить пароль"')
    def click_recovery_button(self):
        self.find_element(RecoveryPageLocators.RECOVERY_PROFILE_BUTTON).click()

    @allure.step('Кликаем на кнопку телефона')
    def click_phone_button(self):
        self.find_element(RecoveryPageLocators.PHONE_BUTTON).click()

    @allure.step('Кликаем на кнопку почты')
    def click_email_button(self):
        self.find_element(RecoveryPageLocators.EMAIL_BUTTON).click()
