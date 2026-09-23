from factories.cycle_factory import create_cycle, create_cycle_group, create_cycle_plan_settings


def test_create_cycle(logged_in_main_page, cycle_page, grouping_page, lookup_page):
    """Проверяет успешное создание цикла"""
    cycle_form_data = create_cycle()
    group_form_data = create_cycle_group()
    cycle_plan_settings = create_cycle_plan_settings(grouping=group_form_data["name"],
                                                     direction=cycle_form_data["direction"])

    cycle_page.open()
    cycle_page.open_add_page()
    cycle_page.fill_cycle_info(form_data=cycle_form_data)
    cycle_page.fill_detail_cycle_channel(conf="Визит к врачу")
    cycle_page.fill_detail_cycle_product(product="Arbidol_Визит к врачу")
    cycle_page.assert_cycle_channel_created()
    cycle_page.assert_cycle_created(cycle_form_data["name"])

    grouping_page.open()
    grouping_page.open_add_page()
    grouping_page.fill_grouping_info(group_form_data)
    grouping_page.fill_detail_product_groupl(product="Arbidol")
    grouping_page.assert_group_created(group_form_data["name"])

    lookup_page.open()
    lookup_page.filter_lookup("Настройки циклового плана")
    lookup_page.open_object_lookup("Настройки циклового плана")
    lookup_page.fill_lookup_info(cycle_plan_settings)

    cycle_page.open()
    cycle_page.open_and_start_cycle(cycle_name=cycle_form_data["name"])