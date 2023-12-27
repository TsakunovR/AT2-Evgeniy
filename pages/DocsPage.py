from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure


class DocsPageLocators:
    RULES_ITEM = (By.XPATH, '//div[@class="rules_links"]')
    FAQ_ITEM = (By.XPATH, '//ul[@class="faq_ul"]')


class DocsPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.check_page()

    @allure.step('Проверяем наличие элементов в форме авторизации')
    def check_page(self):
        self.find_element(DocsPageLocators.RULES_ITEM)
        self.find_element(DocsPageLocators.FAQ_ITEM)
