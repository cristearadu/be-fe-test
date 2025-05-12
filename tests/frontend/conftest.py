import pytest
from playwright.sync_api import sync_playwright, Page, Browser
from core import WEB_BASE_URL


@pytest.fixture(scope="session")
def browser() -> Browser:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser) -> Page:
    context = browser.new_context()
    page = context.new_page()
    page.goto(WEB_BASE_URL)
    yield page
    context.close()
