from selenium.webdriver.common.by import By
from config.settings import BASE_URL
from pages.base_page import BasePage


class CyclePage(BasePage):
    # Локаторы
    ADD_BTN = (By.ID, "ICLCycleSectionSeparateModeAddRecordButtonButton-textEl")
    ADD_PAGE_TITLE = (By.XPATH, "//label[text()='Новая запись']")
    MENU = (By.ID, "menu-button-imageEl")
    CYCLE_NAME = (By.ID, "ICLCyclePageICLName6f890af4-7d9e-4225-a43e-b8b9ad6681d2TextEdit-el")
    CYCLE_START_DATE = (By.ID, "ICLCyclePageICLStartDatea392adba-0c88-4226-92f1-c405baf70b6bDateEdit-el")
    CYCLE_END_DATE = (By.ID, "ICLCyclePageICLEndDate728f1e45-7038-47df-86e2-cc6bb759d745DateEdit-el")
    CYCLE_DIRECTION = (By.ID, "ICLCyclePageICLDirectionOfMedicineLookupEdit-el")
    CYCLE_CHANNEL_ADD_BTN = (By.ID, "ICLCycleChannelDetailAddRecordButtonButton-imageEl")
    RELOAD_BTN = (By.ID, "ICLCycleProductDetailReloadButtonButton-imageEl")
    CYCLE_CHANNEL_PAGE_TITLE = (By.XPATH, "//label[@data-item-marker='Каналы взаимодействия']")
    CYCLE_CHANNEL_CONF = (
        By.ID, "ICLCycleChannelPageICLCycleChannelConf7a815ef7-0c56-4658-935d-aa4bab3d5a82LookupEdit-el")
    CYCLE_PRODUCT_ADD_BTN = (By.ID, "ICLCycleProductDetailAddRecordButtonButton-imageEl")
    CYCLE_PRODUCT_CHOICE = (By.ID, "ICLCycleProductConfLookupEdit-el")
    DETAIL_SAVE_BTN = (By.XPATH, "//span[@data-tag='save']/span")
    CLOSE_BTN = (By.XPATH, "//span[@data-item-marker='CloseButton']")
    CYCLE_CHANEL_DETAIL = (By.XPATH, "//div[@data-item-marker='Номер канала взаимодействия']")

    def get_item_by_marker(self, marker: str):
        """Возвращает элемент с указанным data-item-marker."""
        locator = (By.XPATH, f"//li[@data-item-marker='{marker}']")
        return locator

    def get_span_with_text(self, text: str):
        """Возвращает элемент с указанным data-item-marker."""
        locator = (By.XPATH, f"//span[text()='{text}']")
        return locator

    def open(self):
        """Открывает реестр Цикловые планы"""
        assert self.is_element_displayed(self.MENU)
        super().open(f"{BASE_URL}/0/Nui/ViewModule.aspx#SectionModuleV2/ICLCycleSection/")
        return self

    def open_add_page(self):
        """Открывает карточку добавления цикла"""
        self.click(self.ADD_BTN)
        assert self.is_element_displayed(self.ADD_PAGE_TITLE)

    def fill_cycle_info(self, form_data: dict):
        """Заполняем основную информацию по циклу"""
        self.enter_text(self.CYCLE_NAME, form_data['name'])
        self.enter_text(self.CYCLE_START_DATE, form_data['start_date'])
        self.enter_text(self.CYCLE_END_DATE, form_data['end_date'])
        self.enter_text(self.CYCLE_DIRECTION, form_data['direction'])
        self.is_element_displayed(self.get_item_by_marker(form_data['direction']))
        self.click(self.get_item_by_marker(form_data['direction']))

    def fill_detail_cycle_channel(self, conf):
        self.click(self.CYCLE_CHANNEL_ADD_BTN)
        self.is_element_displayed(self.CYCLE_CHANNEL_PAGE_TITLE)
        self.enter_text(self.CYCLE_CHANNEL_CONF, conf)
        self.is_element_displayed(self.get_item_by_marker(conf))
        self.click(self.get_item_by_marker(conf))

    def fill_detail_cycle_product(self, product):
        self.click(self.CYCLE_PRODUCT_ADD_BTN)
        self.is_element_displayed(self.CYCLE_PRODUCT_CHOICE)
        self.enter_text(self.CYCLE_PRODUCT_CHOICE, product)
        self.is_element_displayed(self.get_item_by_marker(product))
        self.click(self.get_item_by_marker(product))
        self.click(self.DETAIL_SAVE_BTN)
        self.click(self.RELOAD_BTN)
        self.is_element_displayed(self.get_span_with_text(product))

    def assert_cycle_channel_created(self):
        self.click(self.CLOSE_BTN)
        self.is_element_displayed(self.CYCLE_CHANEL_DETAIL)

    def assert_cycle_created(self, name):
        self.click(self.CLOSE_BTN)
        self.is_element_displayed(self.get_span_with_text(name))
