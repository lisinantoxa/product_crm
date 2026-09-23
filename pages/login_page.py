from pages.base_page import BasePage
from config.settings import BASE_URL
from pages.main_page import MainPage


class LoginPage(BasePage):
    USERNAME_INPUT = "#loginEdit-el"
    PASSWORD_INPUT = "#passwordEdit-el"
    LOGIN_BUTTON = "#t-comp14-textEl"
    ERROR_MESSAGE = "[data-test='error']"

    def open(self):
        super().open(f"{BASE_URL}/Login")
        return self

    def login(self, username: str, password: str) -> MainPage:
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return MainPage(self.page)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)