import os
from dotenv import load_dotenv

load_dotenv()

# Базовый URL тестируемого приложения
BASE_URL = os.getenv("BASE_URL", "https://crmpharma-dev.bpm.icl-soft.ru")

# Таймауты
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))  # seconds (unused with Playwright)
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "30"))  # seconds (unused with Playwright)

# Playwright settings
HEADLESS = os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes")

# Данные для тестов (лучше брать из переменных окружения)
DEFAULT_USER = os.getenv("TEST_USER")
DEFAULT_PASSWORD = os.getenv("TEST_PASSWORD")

# Проверка обязательных переменных (выбрасываем понятное исключение если не заданы)
if not DEFAULT_USER or not DEFAULT_PASSWORD:
    raise RuntimeError("Environment variables TEST_USER and TEST_PASSWORD must be set")