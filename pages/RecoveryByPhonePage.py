from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure


class RecoveryByPhonePageLocators:
    COUNTRY_LIST = (By.XPATH, '//div[@data-l="t,country"]')
    COUNTRY_LIST_ITEM = (By.XPATH, '//div[@class ="country-select_i"]')
    PHONE_FIELD = (By.ID, 'field_phone')
    GET_CODE_BUTTON = (By.XPATH, '//*[@data-l="t,submit"]')


class RecoveryByPhonePageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.check_page()

    @allure.step('Проверяем наличие элементов на странице')
    def check_page(self):
        self.find_element(RecoveryByPhonePageLocators.COUNTRY_LIST)
        self.find_element(RecoveryByPhonePageLocators.PHONE_FIELD)
        self.find_element(RecoveryByPhonePageLocators.GET_CODE_BUTTON)

    @allure.step('Открываем выпадающий список стран и возвращаем телефонный код выбранной страны')
    def select_country(self, country_number):
        self.find_element(RecoveryByPhonePageLocators.COUNTRY_LIST).click()
        country_list_item = self.find_elements(RecoveryByPhonePageLocators.COUNTRY_LIST_ITEM)[country_number]
        country_name = country_list_item.get_attribute('data-name')
        COUNTRY_CODE_ELEMENT = (By.XPATH, f'//div[@data-name="{country_name}"]//div[@class="country-select_code"]')
        country_code = self.find_element(COUNTRY_CODE_ELEMENT).text
        country_list_item.click()
        return country_code

    @allure.step('Получаем значение маски телефонного кода в поле "Номер телефона"')
    def get_value(self):
        return self.find_element(RecoveryByPhonePageLocators.PHONE_FIELD).get_attribute('value')
