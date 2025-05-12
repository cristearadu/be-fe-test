import pytest
import requests

from request_builders.request_builder_packages import PackageController
from core import HTTPStatusCodes, default_json_headers, EndpointKeys


class HelperPackage:
    def __init__(self):
        self.controller = PackageController()

    def get_packages(self, access_token: str, **params) -> "requests.Response":
        """
        Retrieve a list of eSIM packages from the API.

        Args:
            access_token (str): Bearer token used for authorization.
            **params: Optional query parameters for filtering packages:
                - filter[type] (str): Filter by type: "local" or "global"
                - filter[country] (str): Filter by ISO country code (e.g., "TR", "US")
                - include (str): Optional data to include, e.g., "topup"
                - limit (int): Max number of packages to return
                - page (int): Page number

        Returns:
            requests.Response: The raw response object from the /packages endpoint.
        """
        headers = default_json_headers(access_token)
        response = self.controller.request(EndpointKeys.GET_PACKAGES.value, headers=headers, params=params)
        return response

    def get_package_and_validate_data(self, access_token: str, expected_status_code: int = HTTPStatusCodes.OK.value,
                                      **params) -> dict:

        get_package_response = self.get_packages(access_token, **params)

        assert get_package_response.status_code == expected_status_code, (
            f"Failed to fetch packages. Expected status {expected_status_code}, got {get_package_response.status_code}"
        )

        pytest.logger.info(f"Fetched packages with params: {params}")
        return get_package_response.json()

    def get_package_id_by_exact_id(self, access_token: str, package_id: str) -> dict | None:
        """
        Search through all countries and operators to find a package with the exact given ID.

        Args:
            access_token (str): A valid OAuth2 bearer token.
            package_id (str): The exact slug (ID) of the eSIM package to find, e.g., "merhaba-7days-1gb".

        Returns:
            dict | None: The full package dictionary if found, otherwise None.

        Example Return:
            {
                "id": "merhaba-7days-1gb",
                "type": "sim",
                "price": 4.5,
                "data": "1 GB",
                "day": 7,
                [...],
            }
        """
        package_response = self.get_package_and_validate_data(access_token)
        for country_data in package_response.get('data', []):
            for operator in country_data.get('operators', []):
                for package in operator.get('packages', []):
                    if package.get('id') == package_id:
                        return package
        return None
