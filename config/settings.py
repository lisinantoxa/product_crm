import os
from dotenv import load_dotenv
load_dotenv()

# Базовый URL тестируемого приложения
BASE_URL = os.getenv("BASE_URL", "https://crmpharma-dev.bpm.icl-soft.ru")

# Таймауты
IMPLICIT_WAIT = 10  # Неявное ожидание (в секундах)
EXPLICIT_WAIT = 30  # Явное ожидание (в секундах)

# Браузер по умолчанию
BROWSER = os.getenv("BROWSER", "chrome")  # chrome, firefox, edge

# Данные для тестов (лучше брать из переменных окружения)
DEFAULT_USER = os.getenv("TEST_USER")
DEFAULT_PASSWORD = os.getenv("TEST_PASSWORD")