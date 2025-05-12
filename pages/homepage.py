from playwright.sync_api import Page
from . import BasePage


class HomePage(BasePage):
    ACCEPT_COOKIES = "//button[@id='onetrust-accept-btn-handler']"
    ALLOW_BUTTON = "//button[normalize-space(text())='ALLOW']"
    SEARCH_INPUT = "//input[@data-testid='search-input']"
    JAPAN_RESULT = "[data-testid='Japan-flag']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.wait_for_element_and_click(self.ACCEPT_COOKIES)
        self.wait_for_element_and_click(self.ALLOW_BUTTON)

    def search_and_select_country(self, country_to_search: str):
        self.fill_text(self.SEARCH_INPUT, country_to_search)
        self.wait_for_element(self.JAPAN_RESULT)
        self.wait_for_element_and_click(self.JAPAN_RESULT)
