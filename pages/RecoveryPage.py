from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure


class RecoveryPageLocators:
    RECOVERY_PROFILE_BUTTON = (By.XPATH, '//button[@data-l="t,restore"]')
    TITTLE_TEXT = (By.LINK_TEXT, 'Восстановление доступа')


class RecoveryPageHelper(BasePage):

    @allure.step('Проверяем наличие элементов в форме авторизации')
    def check_page(self):
        self.find_element(RecoveryPageLocators.RECOVERY_PROFILE_BUTTON)
        self.find_element(RecoveryPageLocators.TITTLE_TEXT)

    @allure.step('Кликаем на кнопку "Восстановить пароль"')
    def click_recovery_button(self):
        self.find_element(RecoveryPageLocators.RECOVERY_PROFILE_BUTTON).click()
