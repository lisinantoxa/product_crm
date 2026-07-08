import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from config.settings import EXPLICIT_WAIT
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, WebDriverException
from typing import List, Optional


class BasePage:
    """Базовый класс для всех Page Objects."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def open(self, url: str):
        """Открывает указанный URL."""
        self.driver.get(url)

    def find_element(self, locator: tuple) -> WebElement:
        """Находит один элемент с явным ожиданием."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator: tuple) -> List[WebElement]:
        """Находит все элементы по локатору."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator: tuple, timeout: int = 10):
        """Кликает на элемент, ожидая, что он кликабелен; на ошибке — fallback через JS; делает скриншот при падении."""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)
        except (TimeoutException, WebDriverException) as exc:
            # можно сделать скриншот здесь: self.driver.save_screenshot(...)
            raise

    def enter_text(self, locator: tuple, text: str):
        """Вводит текст в поле ввода."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Возвращает текст элемента."""
        return self.find_element(locator).text

    def is_element_displayed(self, locator: tuple) -> bool:
        """Проверяет, отображается ли элемент на странице."""
        try:
            return self.find_element(locator).is_displayed()
        except TimeoutException:
            return False

    def is_element_not_present(self, locator, timeout: int = 3) -> bool:
        """
        Проверяет, что элемент отсутствует на странице.
        Возвращает True, если элемент не появился в течение timeout секунд.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return False
        except TimeoutException:
            return True

    def is_element_enabled(self, locator: tuple) -> bool:
        """Проверяет, доступен ли элемент для взаимодействия."""
        try:
            return self.find_element(locator).is_enabled()
        except TimeoutException:
            return False
