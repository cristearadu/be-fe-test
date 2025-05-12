import pytest
from test_data import ORDER_CREATION_CASES
from core import HTTPStatusCodes, ORDER_STATUS
from validators import *


@pytest.mark.backend_test
@pytest.mark.parametrize("case_title, order_payload", ORDER_CREATION_CASES)
def test_create_and_validate_order(main_auth_token, helper_orders, helper_package, helper_esims, case_title,
                                   order_payload):
    """
    Use the endpoint to POST an order for eSIMs using structured input and validate the result.
    """

    package_slug = helper_package.get_package_id_by_exact_id(main_auth_token, order_payload['package_slug'])
    assert package_slug, f"Failed to find the package {order_payload['package_slug']}"

    response = helper_orders.create_esim_order(
        access_token=main_auth_token,
        **order_payload
    )

    assert response.status_code == HTTPStatusCodes.OK.value, (
        f"Expected status {HTTPStatusCodes.CREATED.value}, got {response.status_code}"
    )

    order_data = response.json().get("data", {})
    expected_fields = {
        "package_id": package_slug["id"],
        "type": package_slug["type"],
        "price": package_slug["price"],
        "data": package_slug["data"],
        "validity": package_slug["day"],
        "net_price": package_slug["net_price"]
    }
    validate_order_payload(order_data, expected_fields, order_payload)

    iccid_list = validate_sim_block(order_data.get("sims", []), expected_quantity=order_payload["quantity"])
    esims_response = helper_esims.get_esims_list(
        access_token=main_auth_token,
        include=ORDER_STATUS,
        limit=order_payload['quantity']
    )
    assert esims_response.status_code == HTTPStatusCodes.OK.value
    esims = esims_response.json().get("data", [])
    validate_esim_response(esims, iccid_list, expected_fields)
