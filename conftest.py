import pytest
from playwright.sync_api import Page

from config.settings import DEFAULT_USER, DEFAULT_PASSWORD


@pytest.fixture
def login_page(page: Page):
    """Возвращает LoginPage, построенный на Playwright page."""
    from pages.login_page import LoginPage

    return LoginPage(page)


@pytest.fixture
def main_page(page: Page):
    from pages.main_page import MainPage

    return MainPage(page)


@pytest.fixture
def cycle_page(page: Page):
    from pages.cycle_page import CyclePage

    return CyclePage(page)


@pytest.fixture
def grouping_page(page: Page):
    from pages.grouping_page import GroupingPage

    return GroupingPage(page)

@pytest.fixture
def lookup_page(page: Page):
    from pages.lookup_page import LookupPage

    return LookupPage(page)

@pytest.fixture
def logged_in_main_page(login_page: "LoginPage"):
    """Фикстура, которая выполняет логин и возвращает главную страницу."""
    return login_page.open().login(DEFAULT_USER, DEFAULT_PASSWORD)


# Hook: при падении теста сохранять скриншот страницы (если доступен)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            from pathlib import Path

            artifacts_dir = Path("test-artifacts")
            artifacts_dir.mkdir(exist_ok=True)
            screenshot_path = artifacts_dir / f"{item.name}.png"
            try:
                page.screenshot(path=str(screenshot_path))
            except Exception:
                pass
