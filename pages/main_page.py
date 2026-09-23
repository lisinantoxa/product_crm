from pages.base_page import BasePage


class MainPage(BasePage):
    PAGE_TITLE = "#profile-user-button-imageEl"

    def reestr_with_name(self, name: str):
        return f"xpath=//div[text()='{name}']"

    def reestr_title(self, name: str):
        return f"xpath=//label[text()='{name}']"

    def get_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def is_title_displayed(self) -> bool:
        return self.is_visible(self.PAGE_TITLE)

    def open_reestr(self, name: str):
        return self.click(self.reestr_with_name(name))

    def is_reestr_title_displayed(self, name) -> bool:
        return self.is_visible(self.reestr_title(name))