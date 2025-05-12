from core import CLIENT_ID, CLIENT_SECRET, GrantType


def auth_token_payload(grant_type: str = GrantType.client_credentials.value) -> dict:
    """
    Factory for generating the payload used in the OAuth2 token request.

    Args:
        grant_type (str): The OAuth2 grant type (default: 'client_credentials').

    Returns:
        dict: Payload for the token request.
    """
    return {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": grant_type,
    }


def auth_token_header() -> dict:
    """
    Factory for generating default headers for JSON API requests.

    Returns:
        dict: Standard headers used in most API requests.
    """
    return {"Accept": "application/json"}


def default_json_headers(access_token: str) -> dict:
    """
    Factory for generating default headers for JSON API requests including Authorization.

    Args:
        access_token (str): The bearer token for API access.

    Returns:
        dict: Headers including Accept and Authorization.
    """
    return {"Accept": "application/json", "Authorization": f"Bearer {access_token}"}


def order_payload(**kwargs) -> dict:
    """
    Factory for generating order payload with default values.

    Args:
        **kwargs:
            quantity (int): Number of eSIMs to order (default: 6).
            package_slug (str): The ID of the package to order (default: "merhaba-7days-1gb").
            type (str): Type of SIM (default: "sim").
            description (str): Description of the order.
            brand_settings_name (str): Brand settings name.

    Returns:
        dict: Form-data payload for creating an order.
    """
    return {
        "quantity": str(kwargs.get("quantity", "")),
        "package_id": kwargs.get("package_slug", ""),
        "type": kwargs.get("type", ""),
        "description": kwargs.get("description", ""),
        "brand_settings_name": kwargs.get("brand_settings_name", ""),
    }
