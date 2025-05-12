from enum import Enum
from core import APP_URL, EndpointKeys
from request_builders.request_builder_main import BaseController


class OrderEndpoints(Enum):
    CREATE_ORDER = ("POST", f"{APP_URL}/orders", EndpointKeys.CREATE_ORDER.value)

    def __init__(self, method, path, key):
        self.method = method
        self.path = path
        self.key = key


class OrderController(BaseController):
    endpoints_enum = OrderEndpoints
