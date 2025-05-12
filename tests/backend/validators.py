from core import assert_fields_match


def validate_order_payload(order_data: dict, expected_fields: dict, payload: dict):
    """
        Validates the structure and values of the created order payload.

        Args:
            order_data (dict): The actual order data returned by the API.
            expected_fields (dict): Expected values for certain fields in the order.
            payload (dict): Original request payload used to create the order.

        Raises:
            AssertionError: If any of the order fields do not match the expected values.
    """
    assert order_data.get("package_id") == payload["package_slug"], "Package ID mismatch."
    assert order_data.get("quantity") == payload["quantity"], "Incorrect quantity."
    assert order_data.get("description") == payload["description"], "Incorrect description."

    assert_fields_match(order_data, expected_fields, context="Order → ")
    assert order_data["price"] == expected_fields["price"], "Recommended retail price mismatch (USD)."
    assert order_data["net_price"] == expected_fields["net_price"], "Net price mismatch (USD)."


def validate_sim_block(sims: list, expected_quantity: int) -> list[str]:
    """
    Validates the SIM block returned in the order and extracts ICCIDs.

    Args:
        sims (list): List of SIM objects included in the order.
        expected_quantity (int): Expected number of SIMs in the block.

    Returns:
        list[str]: A list of ICCID strings extracted from the SIMs.

    Raises:
        AssertionError: If any expected field is missing or the quantity is incorrect.
    """
    assert len(sims) == expected_quantity, f"Expected {expected_quantity} SIMs, found {len(sims)}."
    iccids = []
    for i, sim in enumerate(sims):
        for field in ("iccid", "lpa", "qrcode"):
            assert field in sim, f"SIM {i} missing '{field}'."
        assert sim.get("apn_value") == "airalo2", f"SIM {i} has incorrect APN value."
        iccids.append(sim["iccid"])
    return iccids


def validate_esim_response(esims: list, iccid_list: list, expected_fields: dict):
    """
    Validates that eSIMs in the response match the expected values and ICCIDs.

    Args:
        esims (list): List of eSIMs returned from the eSIMs endpoint.
        iccid_list (list): List of expected ICCID values.
        expected_fields (dict): Expected SIM metadata to match against.

    Raises:
        AssertionError: If ICCIDs are missing or SIM metadata doesn't match expectations.
    """
    for sim in esims:
        assert sim["iccid"] in iccid_list, f"Failed to find {sim['id']} in SIM list."
        assert_fields_match(sim["simable"], expected_fields, context="SIMable → ")
