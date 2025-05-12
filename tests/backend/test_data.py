from core import DEFAULT_SIM_TYPE, DEFAULT_APN_VALUE

ORDER_CREATION_CASES = [
    (
        "Create order with 6 Merhaba 7-day eSIMs",
        {
            "quantity": 6,
            "package_slug": "merhaba-7days-1gb",
            "type": DEFAULT_SIM_TYPE,
            "description": None
        }
    )
]