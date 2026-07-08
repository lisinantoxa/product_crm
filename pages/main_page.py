from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    """Page Object для главной страницы."""

    PAGE_TITLE = (By.ID, "profile-user-button-imageEl")

    def reestr_with_name(self, name):
        return By.XPATH, f"//div[text()='{name}']"

    def reestr_title(self, name):
        return By.XPATH, f"//label[text()='{name}']"

    def get_title(self) -> str:
        """Возвращает заголовок главной страницы."""
        return self.get_text(self.PAGE_TITLE)

    def is_title_displayed(self) -> bool:
        """Проверяет, отображается ли заголовок главной страницы."""
        return self.is_element_displayed(self.PAGE_TITLE)

    def open_reestr(self, name: str):
        return self.click(self.reestr_with_name(name))

    def is_reestr_title_displayed(self, name) -> bool:
        """Проверяет, отображается ли заголовок открытого реестра"""
        return self.is_element_displayed(self.reestr_title(name))
