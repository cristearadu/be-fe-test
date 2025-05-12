import pytest
from request_builders import AuthController
from core import auth_token_header, auth_token_payload, HTTPStatusCodes, EndpointKeys


class HelperAuth:
    def __init__(self):
        self.controller = AuthController()

    def get_access_token(
        self, expected_status_code: int = HTTPStatusCodes.OK.value
    ) -> str:
        """
        Obtain OAuth2 access token using client credentials.

        Args:
            expected_status_code (int): Expected HTTP status code (e.g. 200)

        Returns:
            str: Access token string.
        """
        headers = auth_token_header()
        payload = auth_token_payload()

        response = self.controller.request(
            EndpointKeys.AUTH_TOKEN.value, headers=headers, payload=payload
        )

        assert (
            response.status_code == expected_status_code
        ), f"Token fetch failed. Expected status {expected_status_code}, got {response.status_code}"

        data = response.json().get("data", {})
        access_token = data.get("access_token")

        if access_token:
            pytest.logger.info("Successfully obtained access token.")
            return access_token
        else:
            pytest.logger.critical(
                "Access token not found in response. Failing test setup."
            )
            pytest.fail("Missing access token in authentication response.")
