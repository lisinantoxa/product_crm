from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from config.settings import BROWSER

def get_driver(browser_name=None):
    """Создает и возвращает WebDriver для указанного браузера."""
    if browser_name is None:
        browser_name = BROWSER

    if browser_name == "chrome":
        options = ChromeOptions()
        # Добавляем опции для стабильности в CI/CD
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        # Для запуска в headless режиме
        # options.add_argument("--headless=new")
        driver_path = ChromeDriverManager(driver_version="147.0.7727.49").install()
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")

    driver.maximize_window()
    return driver