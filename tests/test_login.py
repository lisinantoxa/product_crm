from config.settings import DEFAULT_USER, DEFAULT_PASSWORD

def test_valid_login(login_page):
    """Проверяет успешный вход в систему."""
    main_page = login_page.open().login(DEFAULT_USER, DEFAULT_PASSWORD)
    assert main_page.is_title_displayed(), "Заголовок главной страницы не отображается."
    main_page.open_reestr(" Цикловые планы ")
    assert main_page.is_reestr_title_displayed("Цикловые планы")

# def test_login_with_empty_username(login_page):
#     """Проверяет ошибку при пустом логине."""
#     login_page.open().login("", DEFAULT_PASSWORD)
#     assert "Epic sadface: Username is required" in login_page.get_error_message()
#
# def test_login_with_empty_password(login_page):
#     """Проверяет ошибку при пустом пароле."""
#     login_page.open().login(DEFAULT_USER, "")
#     assert "Epic sadface: Password is required" in login_page.get_error_message()
#
# def test_login_with_wrong_credentials(login_page):
#     """Проверяет ошибку при неверных учетных данных."""
#     login_page.open().login("invalid_user", "invalid_password")
#     error_text = login_page.get_error_message()
#     assert "Username and password do not match" in error_text, f"Неверное сообщение об ошибке: {error_text}"