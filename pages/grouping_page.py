from playwright.sync_api import expect

from pages.base_page import BasePage
from config.settings import BASE_URL


class GroupingPage(BasePage):
    MENU = "#menu-button-imageEl"
    ADD_BTN = "#ICLGroupingSectionSeparateModeAddRecordButtonButton-textEl"
    ADD_PAGE_TITLE = "xpath=//label[text()='Новая запись']"
    GROUP_NAME = "#ICLGrouping1PageICLName8d10d5f0-ecd1-4422-9943-8c315e06f337TextEdit-el"
    FREQUENCY = "#ICLGrouping1PageICLFrequencyDaysIntegerEdit-el"
    PLANNED_VISIT = "#ICLGrouping1PageICLPlanNumberVisit7d5602b2-beea-4821-8ea1-2bd9f22526a2IntegerEdit-el"
    PLANNED_GOAL = "#ICLGrouping1PageICLPlanNumberTarget2c33106b-c9ec-4eed-a6a5-e5a09ed4a7b5IntegerEdit-el"
    CLIENT_TYPE = "#ICLGrouping1PageICLClientTypeLookupEdit-el"
    GROUP_PRODUCT_ADD_BTN = "#ICLProductGroupingDetailAddRecordButtonButton-imageEl"
    GROUP_PRODUCT_CHOICE = "#ICLProductLookupEdit-el"
    DETAIL_SAVE_BTN = "xpath=//span[@data-tag='save']/span"
    RELOAD_BTN = "#ICLProductGroupingDetailReloadButtonButton-imageEl"
    CLOSE_BTN = "xpath=//span[@data-item-marker='CloseButton']"
    SAVE_BTN = "#ICLGrouping1PageSaveButtonButton-textEl"

    def get_item_by_marker(self, marker: str):
        return f"xpath=//div[@data-item-marker='{marker}']"

    def get_span_with_text(self, text: str):
        return f"xpath=//span[text()='{text}']"

    def open(self):
        assert self.is_visible(self.MENU)
        super().open(f"{BASE_URL}/0/Nui/ViewModule.aspx#SectionModuleV2/ICLGroupingSection/")
        return self

    def open_add_page(self):
        self.click(self.ADD_BTN)
        assert self.is_visible(self.ADD_PAGE_TITLE)

    def fill_grouping_info(self, form_data: dict):
        self.fill(self.GROUP_NAME, str(form_data['name']))
        self.fill(self.FREQUENCY, str(form_data['freq']))
        self.fill(self.PLANNED_VISIT, str(form_data['planned_visit']))
        self.fill(self.PLANNED_GOAL, str(form_data['planned_goal']))
        self.fill_with_enter(self.CLIENT_TYPE, form_data['client_type'])
        self.wait_for(self.get_item_by_marker(form_data['client_type']))
        self.dblclick(self.get_item_by_marker(form_data['client_type']))

    def fill_detail_product_groupl(self, product: str):
        self.click(self.GROUP_PRODUCT_ADD_BTN)
        assert self.is_visible(self.GROUP_PRODUCT_CHOICE)
        self.fill_with_enter(self.GROUP_PRODUCT_CHOICE, product)
        self.wait_for(self.get_item_by_marker(product))
        self.dblclick(self.get_item_by_marker(product))
        self.click(self.get_span_with_text(product))
        self.click(self.DETAIL_SAVE_BTN)
        self.click(self.RELOAD_BTN)
        assert self.is_visible(self.get_span_with_text(product))

    def assert_group_created(self, name: str):
        self.click(self.CLOSE_BTN)
        assert self.is_visible(self.get_span_with_text(name))