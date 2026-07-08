from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import BASE_URL

class LoginPage(BasePage):
    """Page Object для страницы авторизации."""

    # Локаторы
    USERNAME_INPUT = (By.ID, "loginEdit-el")
    PASSWORD_INPUT = (By.ID, "passwordEdit-el")
    LOGIN_BUTTON = (By.ID, "t-comp14-textEl")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        """Открывает страницу логина."""
        super().open(f"{BASE_URL}/Login")
        return self

    def login(self, username: str, password: str):
        """Выполняет авторизацию с указанными учетными данными."""
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self.driver

    def get_error_message(self) -> str:
        """Возвращает текст сообщения об ошибке."""
        return self.get_text(self.ERROR_MESSAGE)