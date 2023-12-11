import allure
import pytest
from selenium import webdriver
from pages.BasePage import BasePage

URL = "https://ok.ru"


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title(f"Открываем браузер и переходим на страницу: {URL}")
@pytest.fixture
def open_base_url(browser):
    base_page = BasePage(browser)
    base_page.go_to_url(URL)
