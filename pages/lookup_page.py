from pages.base_page import BasePage
from config.settings import BASE_URL


class LookupPage(BasePage):
    # селекторы как строки
    MENU = "#menu-button-imageEl"
    ADD_BTN = "#BaseLookupConfigurationSectionSeparateModeAddRecordButtonButton-textEl"
    FILTER_CLOSE_BTN = "xpath=//span[@data-tag='customFilterName_Lookup']"
    QUICK_FILTER_OPEN_BTN = "#QuickFilterModuleContainer"
    QUICK_FILTER_CHOOSE = "xpath=//li[@data-item-marker='Добавить условие']"
    QUICK_FILTER_FIELD = "#customFilterSectionModuleV2_LookupSection_QuickFilterModuleV2-el"
    APPLY_BTN = "xpath=//span[@data-item-marker='applyButton']"
    LOOKUP_PAGE_TITLE = "xpath=//label[text()='Новая запись']"
    LOOKUP_CYCLE_PLAN_SETT_NAME = "#NameTextEdit-el"
    LOOKUP_CYCLE_PLAN_SETT_DIRECTION = "#ICLDirectionLookupEdit-el"
    LOOKUP_CYCLE_PLAN_SETT_GROUPING = "#ICLGroupingLookupEdit-el"
    SAVE_LOOKUP_RECORD = "xpath=//span[@data-item-marker='save']"
    PRELOADER = "xpath=//div[@class='ts-mask-spinner']"


    def get_item_by_marker(self, marker: str):
        return f"xpath=//div[@data-item-marker='{marker}'][1]"

    def get_label_with_text(self, text: str):
        return f"xpath=//label[text()='{text}']"

    def get_span_with_text(self, text: str):
        return f"xpath=(//span[text()='{text}'])[1]"

    def open(self):
        assert self.is_visible(self.MENU)
        super().open(f"{BASE_URL}/0/Nui/ViewModule.aspx#SectionModuleV2/LookupSection")
        return self

    def filter_lookup(self, lookup_name):
        self.click(self.FILTER_CLOSE_BTN)
        assert self.wait_for(self.FILTER_CLOSE_BTN, state="hidden")
        self.click(self.QUICK_FILTER_OPEN_BTN)
        self.click(self.QUICK_FILTER_CHOOSE)
        self.fill(self.QUICK_FILTER_FIELD, lookup_name)
        self.click(self.APPLY_BTN)
        assert self.wait_for(self.get_item_by_marker(lookup_name))

    def open_object_lookup(self, lookup_name):
        self.click(self.get_span_with_text(lookup_name))
        assert self.wait_for(self.get_label_with_text(lookup_name))

    def fill_lookup_info(self, lookup_info):
        self.click(self.ADD_BTN)
        self.fill(self.LOOKUP_CYCLE_PLAN_SETT_NAME, str(lookup_info['name']))
        self.fill_with_enter(self.LOOKUP_CYCLE_PLAN_SETT_GROUPING, lookup_info['grouping'])
        self.wait_for(self.get_item_by_marker(lookup_info['grouping']))
        self.dblclick(self.get_item_by_marker(lookup_info['grouping']))
        self.click(self.get_item_by_marker(str(lookup_info['name'])))
        self.fill_with_enter(self.LOOKUP_CYCLE_PLAN_SETT_DIRECTION, lookup_info['direction'])
        self.wait_for(self.get_item_by_marker(lookup_info['direction']))
        self.dblclick(self.get_item_by_marker(lookup_info['direction']))
        self.click(self.get_item_by_marker(str(lookup_info['name'])))
        self.click(self.SAVE_LOOKUP_RECORD)
        self.wait_for(self.PRELOADER, state="hidden")
