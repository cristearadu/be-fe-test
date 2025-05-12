

def assert_fields_match(actual: dict, expected: dict, context: str = ""):
    for field, expected_value in expected.items():
        actual_value = actual.get(field)
        assert str(actual_value) == str(expected_value), (
            f"{context}{field} mismatch. Expected: {expected_value}, Got: {actual_value}"
        )

