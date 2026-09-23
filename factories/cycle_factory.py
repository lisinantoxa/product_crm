from datetime import datetime, timedelta
import random


def create_cycle():
    today = datetime.now()
    return {
        "name": f"Цикл тестовый {random.randint(1000, 9999)}",
        "start_date": today.strftime("%d.%m.%Y"),
        "end_date": (today + timedelta(days=14)).strftime("%d.%m.%Y"),
        "direction": "BIOPHARMA_PM"
    }


def create_cycle_group():
    return {
        "name": f"Группировка А {random.randint(1000, 9999)}",
        "freq": 1,
        "planned_visit": 1,
        "planned_goal": 1,
        "client_type": "Клиент",
    }

def create_cycle_plan_settings(direction,grouping):
    return {
        "name": f"Тест {random.randint(1000, 9999)}",
        "grouping": grouping,
        "direction": direction
    }
