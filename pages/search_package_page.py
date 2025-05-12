from . import BasePage
from playwright.sync_api import Page
from core import COMMON_PACKAGE_DETAIL_LOCATORS, DetailLocators, WebUIDataTypes


class SearchPackagePage(BasePage):
    SIM_PACKAGE_ITEM = f"//a[@{WebUIDataTypes.DATA_TEST_ID.value}='{DetailLocators.SIM_PACKAGE_ITEM.value}']"
    DETAIL_LOCATORS = {
        f"{DetailLocators.OPERATOR_TITLE.value.replace('-','_')}":
            f"//div//p[@{WebUIDataTypes.DATA_TEST_ID.value}='{DetailLocators.OPERATOR_TITLE.value}']",
        **{k: f"//div//{v}" for k, v in COMMON_PACKAGE_DETAIL_LOCATORS.items()},
        DetailLocators.GET_FREE_ESIM_BUTTON.value: "//button"
    }

    def __init__(self, page: Page):
        super().__init__(page)

    def get_package_details_by_index(self, index: int = 1) -> dict:
        return self.extract_details(
            {
                key: self.compose_xpath_with_index(self.SIM_PACKAGE_ITEM, detail_xpath, index)
                for key, detail_xpath in self.DETAIL_LOCATORS.items()
            },
            skip_keys=[DetailLocators.GET_FREE_ESIM_BUTTON.value]
        )

    def click_get_free_esim_by_index(self, index: int = 1):
        self.get_indexed_locator(
            self.SIM_PACKAGE_ITEM,
            self.DETAIL_LOCATORS[DetailLocators.GET_FREE_ESIM_BUTTON.value],
            index
        ).click()
