from playwright.sync_api import Page
from . import BasePage
from core import COMMON_PACKAGE_DETAIL_LOCATORS, DetailLocators, WebUIDataTypes

BASE_CART_SCREEN = f"//div[@{WebUIDataTypes.DATA_TEST_ID.value}='{DetailLocators.SIM_DETAIL_HEADER.value}']"


class CartPage(BasePage):
    DETAIL_LOCATORS = {
        "operator_title": f"{BASE_CART_SCREEN}//div[@{WebUIDataTypes.DATA_TEST_ID.value}='{DetailLocators.SIM_DETAIL_OPERATOR_TITLE.value}']",
        **{k: f"{BASE_CART_SCREEN}//{v}" for k, v in COMMON_PACKAGE_DETAIL_LOCATORS.items()}
    }

    def __init__(self, page: Page):
        super().__init__(page)

    def get_cart_details(self) -> dict:
        return self.extract_details(self.DETAIL_LOCATORS)

