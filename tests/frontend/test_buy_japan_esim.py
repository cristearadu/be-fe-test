import pytest
from pages import HomePage, SearchPackagePage, CartPage
from core import assert_fields_match


@pytest.mark.parametrize("country_name", ["Japan"])
@pytest.mark.frontend_test
def test_buy_japan_esim_package(page, country_name):
    """
    End-to-end test for one step before purchasing a Japan eSIM package on Airalo.

    Steps:
    1. Navigate to the homepage.
    2. Search for "Japan" in the country search input.
    3. Select the first available eSIM package from the search results.
    4. Click the first eSIM offer.
    5. On the cart page, verify that the package details (title, coverage, data, validity, price)
       match those from the selected package.

    Assertion:
    - Ensures consistency of selected eSIM data from search to cart.
    """
    pytest.logger.info(f"Navigating to homepage and searching for: {country_name}")
    homepage = HomePage(page)
    homepage.search_and_select_country(country_name)

    pytest.logger.info("Selecting first available package from search results.")
    package_page = SearchPackagePage(page)
    package_info = package_page.get_package_details_by_index()
    pytest.logger.info(f"Captured package details: {package_info}")
    package_page.click_get_free_esim_by_index()

    pytest.logger.info("Navigating to cart and retrieving package details.")
    cart_page = CartPage(page)
    cart_package_details = cart_page.get_cart_details()
    pytest.logger.info(f"Cart package details: {cart_package_details}")

    pytest.logger.info("Asserting selected package matches cart contents.")
    assert_fields_match(package_info, cart_package_details)

