from enum import Enum


class DetailLocators(Enum):
    OPERATOR_TITLE = "operator-title"
    COVERAGE = "COVERAGE-value"
    DATA = "DATA-value"
    VALIDITY = "VALIDITY-value"
    PRICE = "PRICE-value"
    GET_FREE_ESIM_BUTTON = 'get_free_esim_button'
    SIM_PACKAGE_ITEM = 'sim-package-item'
    SIM_DETAIL_HEADER = 'sim-detail-header'
    SIM_DETAIL_OPERATOR_TITLE = 'sim-detail-operator-title'


COMMON_PACKAGE_DETAIL_LOCATORS = {
    "coverage": "p[@data-testid='COVERAGE-value']",
    "data": "p[@data-testid='DATA-value']",
    "validity": "p[@data-testid='VALIDITY-value']",
    "price": "p[@data-testid='PRICE-value']"
}