from config.settings import DEFAULT_USER, DEFAULT_PASSWORD


def test_valid_login(login_page):
    """Проверяет успешный вход в систему."""
    main_page = login_page.open().login(DEFAULT_USER, DEFAULT_PASSWORD)
    assert main_page.is_title_displayed(), "Заголовок главной страницы не отображается."


import pytest

@pytest.mark.parametrize(
    "username,password,expect_success",
    [
        (DEFAULT_USER, DEFAULT_PASSWORD, True),
        ("", DEFAULT_PASSWORD, False),
        (DEFAULT_USER, "", False),
        ("invalid_user", "invalid_password", False),
    ],
)
def test_login_various(login_page, username, password, expect_success):
    login_page.open()
    if expect_success:
        main_page = login_page.login(username, password)
        assert main_page.is_title_displayed()
    else:
        login_page.login(username, password)
        assert login_page.get_error_message() != ""