from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    PROFILE_TAB = (By.XPATH, '//*[@data-l="t,profiles_tab"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_INPUT = (By.ID, 'field_email')
    PASSWORD_INPUT = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    RECOVERY_BUTTON = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTER_BUTT0N = (By.XPATH, '//*[@class="button-pro __sec mb-3x"]')
    VK_BUTTON = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAILRU_BUTTON = (By.XPATH, 'data-l="t,mailru"')
    GOOGLE_BUTTON = (By.XPATH, '//*[@data-l="t,google"]')
    YANDEX_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    APPLE_BUTTON = (By.XPATH, '//*[@data-l="t,apple"]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON)