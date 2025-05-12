from request_builders import OrderController
from core import default_json_headers, order_payload, EndpointKeys


class HelperOrders:
    def __init__(self):
        self.controller = OrderController()

    def create_esim_order(self, access_token: str, **kwargs):
        """
        Create an order for eSIMs using the given access token and input parameters.

        Args:
            access_token (str): Bearer token for authorization.
            **kwargs:
                quantity (int, optional): Number of eSIMs to order (default: 6).
                package_slug (str, optional): The ID of the package to order (default: "merhaba-7days-1gb").
                type (str, optional): Type of SIM (default: "sim").
                description (str, optional): Description of the order (default: "Example description to identify the order").
                brand_settings_name (str, optional): Brand settings name (default: "our perfect brand").

        Returns:
            Response: The response object from the POST request.
        """
        headers = default_json_headers(access_token)
        payload = order_payload(**kwargs)
        response = self.controller.request(
            EndpointKeys.CREATE_ORDER.value, headers=headers, payload=payload
        )
        return response
