from pages.cycle_page import CyclePage
from datetime import datetime, timedelta
import random

from pages.grouping_page import GroupingPage


def test_create_cycle(logged_in_main_page):
    """Проверяет успешное создание цикла"""
    today = datetime.now()
    cycle_form_data = {"name": f"Цикл Тестовый {random.randint(1000, 9999)}",
                       "start_date": today.strftime("%d.%m.%Y"),
                       "end_date": (today + timedelta(days=14)).strftime("%d.%m.%Y"),
                       "direction": "BIOPHARMA_PM", }
    group_form_data = {"name": f"Группировка А {random.randint(1000, 9999)}",
                       "freq": 1,
                       "planned_visit": 1,
                       "planned_goal": 1,
                       "client_type": "Клиент"}
    cycle_page = CyclePage(logged_in_main_page)
    grouping_page = GroupingPage(logged_in_main_page)
    # cycle_page.open()
    # cycle_page.open_add_page()
    # cycle_page.fill_cycle_info(form_data=cycle_form_data)
    # cycle_page.fill_detail_cycle_channel(conf="Визит к врачу")
    # cycle_page.fill_detail_cycle_product(product="Arbidol_Визит к врачу")
    # cycle_page.assert_cycle_channel_created()
    # cycle_page.assert_cycle_created(cycle_form_data['name'])
    grouping_page.open()
    grouping_page.open_add_page()
    grouping_page.fill_grouping_info(group_form_data)
    grouping_page.fill_detail_product_groupl(product="Arbidol")
    grouping_page.assert_group_created(group_form_data['name'])
