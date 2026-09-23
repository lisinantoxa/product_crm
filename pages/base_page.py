from playwright.sync_api import Page, expect
from typing import Optional


class BasePage:
    """Базовый класс для Page Objects на Playwright.

    Использует строковые селекторы (CSS, xpath=..., text=...).
    """

    def __init__(self, page: Page, base_url: Optional[str] = None):
        self.page = page
        self.base_url = base_url or ""

    def open(self, url: str):
        self.page.goto(url)
        return self

    def locator(self, selector: str):
        return self.page.locator(selector)

    def click(self, selector: str, timeout: int = 30000):
        """Кликает по элементу через locator API и ждёт, пока действие выполнится."""
        self.page.locator(selector).click(timeout=timeout)
        return self

    def dblclick(self, selector: str, timeout: int = 30000):
        """Кликает по элементу через locator API и ждёт, пока действие выполнится."""
        self.page.locator(selector).dblclick(timeout=timeout)
        return self

    def fill(self, selector: str, text: str, timeout: int = 30000):
        self.page.locator(selector).fill(text, timeout=timeout)
        return self

    def fill_with_enter(self, selector: str, text: str, timeout: int = 30000):
        self.page.locator(selector).press_sequentially(text, timeout=timeout)
        self.page.locator(selector).press("Enter")
        return self

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector: str, timeout: int = 20000) -> bool:
        try:
            self.page.locator(selector).wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False

    def wait_for(self, selector: str, state: str = "visible", timeout: int = 30000):
        self.page.locator(selector).wait_for(state=state, timeout=timeout)
        return self

    def wait_until_enabled(self, selector: str, timeout: int = 15000, check_initially_disabled: bool = True) -> None:
        """
        Убедиться, что элемент (кнопка) сначала задизейблен (если check_initially_disabled=True),
        и станет активным (enabled) в течение timeout миллисекунд.
        """
        locator = self.page.locator(selector)

        # опционально проверить, что элемент изначально disabled
        if check_initially_disabled:
            # короткий таймаут — проверяем что он disabled прямо сейчас
            expect(locator).to_contain_class("t-btn-disabled", timeout=1000)

        # ждём, пока элемент не станет enabled в пределах timeout
        expect(locator).not_to_contain_class("t-btn-disabled",timeout=timeout)
