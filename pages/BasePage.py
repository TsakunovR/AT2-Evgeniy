from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as ec
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=5):
        return WDW(self.driver, time).until(ec.presence_of_element_located(locator),
                                            message=f'Не смогли дождаться элемент {locator}')

    def find_elements(self, locator, time=5):
        return WDW(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                            message=f'Не смогли дождаться элементы {locator}')

    def go_to_url(self, url):
        return self.driver.get(url)

    @allure.step('Проверяем переход на страницу "Восстановление доступа"')
    def get_url(self):
        return self.driver.current_url
