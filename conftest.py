import pytest
from selenium import webdriver

from pages.cycle_page import CyclePage
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from config.settings import DEFAULT_USER, DEFAULT_PASSWORD

@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия драйвера."""
    driver_instance = get_driver()
    yield driver_instance
    driver_instance.quit()

@pytest.fixture
def login_page(driver):
    """Фикстура для предоставления объекта LoginPage."""
    return LoginPage(driver)

@pytest.fixture
def cycle_page(driver):
    """Фикстура для предоставления объекта CyclePage."""
    from pages.cycle_page import CyclePage
    return CyclePage(driver)

@pytest.fixture
def main_page(driver):
    """Фикстура для предоставления объекта MainPage."""
    from pages.main_page import MainPage
    return MainPage(driver)

@pytest.fixture
def logged_in_main_page(login_page):
    """Фикстура, которая выполняет логин и возвращает главную страницу."""
    return login_page.open().login(DEFAULT_USER, DEFAULT_PASSWORD)