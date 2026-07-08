from time import sleep

from selenium.webdriver.common.by import By
from config.settings import BASE_URL
from pages.base_page import BasePage


class GroupingPage(BasePage):
    # Локаторы
    MENU = (By.ID, "menu-button-imageEl")
    ADD_BTN = (By.ID, "ICLGroupingSectionSeparateModeAddRecordButtonButton-textEl")
    ADD_PAGE_TITLE = (By.XPATH, "//label[text()='Новая запись']")
    GROUP_NAME = (By.ID, "ICLGrouping1PageICLName8d10d5f0-ecd1-4422-9943-8c315e06f337TextEdit-el")
    FREQUENCY = (By.ID, "ICLGrouping1PageICLFrequencyDaysIntegerEdit-el")
    PLANNED_VISIT = (By.ID, "ICLGrouping1PageICLPlanNumberVisit7d5602b2-beea-4821-8ea1-2bd9f22526a2IntegerEdit-el")
    PLANNED_GOAL = (By.ID, "ICLGrouping1PageICLPlanNumberTarget2c33106b-c9ec-4eed-a6a5-e5a09ed4a7b5IntegerEdit-el")
    CLIENT_TYPE = (By.ID, "ICLGrouping1PageICLClientTypeLookupEdit-el")
    GROUP_PRODUCT_ADD_BTN = (By.ID, "ICLProductGroupingDetailAddRecordButtonButton-imageEl")
    GROUP_PRODUCT_CHOICE = (By.ID, "ICLProductLookupEdit-el")
    DETAIL_SAVE_BTN = (By.XPATH, "//span[@data-tag='save']/span")
    RELOAD_BTN = (By.ID, "ICLProductGroupingDetailReloadButtonButton-imageEl")
    CLOSE_BTN = (By.XPATH, "//span[@data-item-marker='CloseButton']")
    SAVE_BTN = (By.ID, "ICLGrouping1PageSaveButtonButton-textEl")

    def get_item_by_marker(self, marker: str):
        """Возвращает элемент с указанным data-item-marker."""
        locator = (By.XPATH, f"//li[@data-item-marker='{marker}']")
        return locator

    def get_span_with_text(self, text: str):
        """Возвращает элемент с указанным data-item-marker."""
        locator = (By.XPATH, f"//span[text()='{text}']")
        return locator

    def open(self):
        """Открывает реестр Группирровка"""
        assert self.is_element_displayed(self.MENU)
        super().open(f"{BASE_URL}/0/Nui/ViewModule.aspx#SectionModuleV2/ICLGroupingSection/")
        return self

    def open_add_page(self):
        """Открывает карточку добавления группировки"""
        self.click(self.ADD_BTN)
        assert self.is_element_displayed(self.ADD_PAGE_TITLE)

    def fill_grouping_info(self, form_data: dict):
        """Заполняем основную информацию по группировку"""
        self.enter_text(self.GROUP_NAME, form_data['name'])
        self.enter_text(self.FREQUENCY, form_data['freq'])
        self.enter_text(self.PLANNED_VISIT, form_data['planned_visit'])
        self.enter_text(self.PLANNED_GOAL, form_data['planned_goal'])
        self.enter_text(self.CLIENT_TYPE, form_data['client_type'])
        self.is_element_displayed(self.get_item_by_marker(form_data['client_type']))
        self.click(self.get_item_by_marker(form_data['client_type']))
        # self.click(self.SAVE_BTN)
        # self.is_element_displayed(self.CLOSE_BTN)

    def fill_detail_product_groupl(self, product):
        """Заполняем деталь Продукт в группировке"""
        sleep(5)
        self.click(self.GROUP_PRODUCT_ADD_BTN)
        self.is_element_displayed(self.GROUP_PRODUCT_CHOICE)
        self.enter_text(self.GROUP_PRODUCT_CHOICE, product)
        self.is_element_displayed(self.get_item_by_marker(product))
        self.click(self.get_item_by_marker(product))
        self.click(self.DETAIL_SAVE_BTN)
        self.click(self.RELOAD_BTN)
        self.is_element_displayed(self.get_span_with_text(product))

    def assert_group_created(self, name):
        self.click(self.CLOSE_BTN)
        self.is_element_displayed(self.get_span_with_text(name))
