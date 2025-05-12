import pytest
from playwright.sync_api import Page
from core import Timeout


class BasePage:
    """
    BasePage provides common utilities for interacting with web elements using Playwright.

    This class encapsulates reusable actions like clicking, waiting for elements, filling input fields,
    and extracting multiple fields by XPath. It's designed to be extended by more specific page objects.

    Attributes:
        page (Page): Playwright page instance for interacting with the browser.
    """
    def __init__(self, page: Page):
        """
        Initializes the BasePage with a Playwright page instance.

        Args:
            page (Page): Playwright page object.
        """
        self.page = page

    def click(self, selector: str):
        """
        Clicks on the element matching the given selector.

        Args:
            selector (str): XPath or CSS selector to locate the element.
        """
        pytest.logger.info(f"Clicking on: {selector}")
        self.page.locator(selector).click()

    def wait_for_element(self, selector: str, timeout: int = Timeout.DEFAULT.value):
        """
        Waits until the element is visible in the DOM.

        Args:
            selector (str): Selector to wait for.
            timeout (int): Time to wait before failing (default from Timeout).
        """
        self.page.wait_for_selector(selector, timeout=timeout)

    def wait_for_element_and_click(self, selector: str, timeout: int = Timeout.DEFAULT.value):
        """
        Waits for the element to appear and then clicks it.

        Args:
            selector (str): Selector of the element to wait for and click.
            timeout (int): Timeout for waiting (default from Timeout).
        """
        self.page.wait_for_selector(selector, timeout=timeout)
        self.click(selector)

    def fill_text(self, selector: str, text: str, timeout: int = Timeout.DEFAULT.value):
        """
        Waits for the element and fills it with the provided text.

        Args:
            selector (str): Selector of the input element.
            text (str): Text to fill into the element.
            timeout (int): Timeout for waiting (default from Timeout).
        """
        pytest.logger.info(f"Filling {selector} with: {text}")
        self.wait_for_element(selector, timeout)
        self.page.locator(selector).fill(text)

    def wait_and_scroll_to_element(self, selector: str, timeout: int = Timeout.DEFAULT.value):
        """
        Waits for the element and scrolls it into view.

        Args:
            selector (str): Selector of the element to scroll to.
            timeout (int): Timeout for waiting (default from Timeout).
        """
        self.wait_for_element(selector, timeout=timeout)
        self.page.locator(selector).evaluate("element => element.scrollIntoView()")

    def extract_details(self, locator_map: dict, skip_keys: list[str] = None) -> dict:
        """
        Extracts text details from multiple elements defined by XPath locators.

        Args:
            locator_map (dict): Mapping of keys to XPath locators.
            skip_keys (list[str], optional): Keys to skip extracting. Defaults to None.

        Returns:
            dict: Extracted text values keyed by the locator_map keys.
        """
        skip_keys = skip_keys or []
        return {
            key: self.page.locator(xpath).inner_text()
            for key, xpath in locator_map.items()
            if key not in skip_keys
        }

    def compose_xpath_with_index(self, base_xpath: str, detail_xpath: str, index: int = 1) -> str:
        """
        Composes an XPath expression combining base, detail, and index.

        Args:
            base_xpath (str): Base XPath expression.
            detail_xpath (str): Detail XPath to append.
            index (int): Index to select among multiple matches (1-based).

        Returns:
            str: Composed XPath string.
        """
        return f"({base_xpath})[{index}]{detail_xpath}"

    def get_indexed_locator(self, base_xpath: str, detail_xpath: str, index: int = 1):
        """
        Returns a locator for the element at the specified index within the composed XPath.

        Args:
            base_xpath (str): Base XPath expression.
            detail_xpath (str): Detail XPath to append.
            index (int): Index of the element (1-based).

        Returns:
            Locator: Playwright locator for the indexed element.
        """
        return self.page.locator(self.compose_xpath_with_index(base_xpath, detail_xpath, index))
