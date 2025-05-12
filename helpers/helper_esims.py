from request_builders import EsimController
from core import HTTPStatusCodes, EndpointKeys
from core.payload_factory import default_json_headers


class HelperEsims:
    def __init__(self):
        self.controller = EsimController()

    def get_esims_list(self, access_token: str, **params) -> dict:
        """
        Fetch the list of eSIMs for the authorized partner.

        Args:
            access_token (str): Valid OAuth2 bearer token.
            expected_status_code (int): Expected HTTP status code for the request.
            **params: Optional query parameters for filtering or including related data.
                - include: comma-separated string (e.g. "order,order.status")
                - filter[created_at]: date string (Y-m-d or Y-m-d - Y-m-d)
                - filter[iccid]: ICCID string
                - limit: int (how many sims to return)

        Returns:
            dict: JSON response body from the eSIMs list API.
        """
        headers = default_json_headers(access_token)
        response = self.controller.request(EndpointKeys.LIST_ESIMS.value, headers=headers, payload=params)
        return response
