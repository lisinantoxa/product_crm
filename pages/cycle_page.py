from pages.base_page import BasePage
from config.settings import BASE_URL


class CyclePage(BasePage):
    # селекторы как строки
    ADD_BTN = "#ICLCycleSectionSeparateModeAddRecordButtonButton-textEl"
    ADD_PAGE_TITLE = "xpath=//label[text()='Новая запись']"
    MENU = "#menu-button-imageEl"
    CYCLE_NAME = "#ICLCyclePageICLName6f890af4-7d9e-4225-a43e-b8b9ad6681d2TextEdit-el"
    CYCLE_START_DATE = "#ICLCyclePageICLStartDatea392adba-0c88-4226-92f1-c405baf70b6bDateEdit-el"
    CYCLE_END_DATE = "#ICLCyclePageICLEndDate728f1e45-7038-47df-86e2-cc6bb759d745DateEdit-el"
    CYCLE_DIRECTION = "#ICLCyclePageICLDirectionOfMedicineLookupEdit-el"
    CYCLE_CHANNEL_ADD_BTN = "#ICLCycleChannelDetailAddRecordButtonButton-imageEl"
    RELOAD_BTN = "#ICLCycleProductDetailReloadButtonButton-imageEl"
    CYCLE_CHANNEL_PAGE_TITLE = "xpath=//label[@data-item-marker='Каналы взаимодействия']"
    CYCLE_CHANNEL_CONF = "#ICLCycleChannelPageICLCycleChannelConf7a815ef7-0c56-4658-935d-aa4bab3d5a82LookupEdit-el"
    CYCLE_PRODUCT_ADD_BTN = "#ICLCycleProductDetailAddRecordButtonButton-imageEl"
    CYCLE_PRODUCT_CHOICE = "#ICLCycleProductConfLookupEdit-el"
    DETAIL_SAVE_BTN = "xpath=//span[@data-tag='save']/span"
    CLOSE_BTN = "xpath=//span[@data-item-marker='CloseButton']"
    CYCLE_CHANEL_DETAIL = "xpath=//div[@data-item-marker='Номер канала взаимодействия']"
    CYCLE_START_BTN = "#ICLCycleSectionICLCalculateCyclePlansButtonButton-textEl"
    MODAL_SCREEN_OK_BTN = "xpath=//span[@data-item-marker='']"

    def get_item_by_marker(self, marker: str):
        return f"xpath=//div[@data-item-marker='{marker}']"

    def get_span_with_text(self, text: str):
        return f"xpath=//span[text()='{text}']"

    def get_div_with_text(self, text: str):
        return f"xpath=//div[text()='{text}']"

    def open(self):
        assert self.is_visible(self.MENU)
        super().open(f"{BASE_URL}/0/Nui/ViewModule.aspx#SectionModuleV2/ICLCycleSection/")
        return self

    def open_add_page(self):
        self.click(self.ADD_BTN)
        assert self.is_visible(self.ADD_PAGE_TITLE)

    def fill_cycle_info(self, form_data: dict):
        self.fill(self.CYCLE_NAME, form_data["name"])
        self.fill(self.CYCLE_START_DATE, form_data["start_date"])
        self.fill(self.CYCLE_END_DATE, form_data["end_date"])
        self.fill_with_enter(self.CYCLE_DIRECTION, form_data["direction"])
        self.wait_for(self.get_item_by_marker(form_data["direction"]))
        self.dblclick(self.get_item_by_marker(form_data["direction"]))

    def fill_detail_cycle_channel(self, conf: str):
        self.click(self.CYCLE_CHANNEL_ADD_BTN)
        assert self.is_visible(self.CYCLE_CHANNEL_CONF)
        self.fill_with_enter(self.CYCLE_CHANNEL_CONF, conf)
        self.wait_for(self.get_item_by_marker(conf))
        self.dblclick(self.get_item_by_marker(conf))

    def fill_detail_cycle_product(self, product: str):
        self.click(self.CYCLE_PRODUCT_ADD_BTN)
        assert self.is_visible(self.CYCLE_PRODUCT_CHOICE)
        self.fill_with_enter(self.CYCLE_PRODUCT_CHOICE, product)
        self.wait_for(self.get_item_by_marker(product))
        self.dblclick(self.get_item_by_marker(product))
        self.click(self.get_span_with_text(product))
        self.click(self.DETAIL_SAVE_BTN)
        self.click(self.RELOAD_BTN)
        assert self.is_visible(self.get_span_with_text(product))

    def assert_cycle_channel_created(self):
        self.click(self.CLOSE_BTN)
        assert self.is_visible(self.CYCLE_CHANEL_DETAIL)

    def assert_cycle_created(self, name: str):
        self.click(self.CLOSE_BTN)
        assert self.is_visible(self.get_span_with_text(name))

    def open_and_start_cycle(self, cycle_name):
        self.click(self.get_span_with_text(cycle_name))
        self.click(self.CYCLE_START_BTN)
        assert self.is_visible(self.get_div_with_text(
            text="Процесс создания цикловых планов запущен. По завершению вам поступит уведомление в боковую панель."))
        self.click(self.get_span_with_text(text="ОК"))
        self.wait_until_enabled(self.CYCLE_START_BTN, timeout=15000)
