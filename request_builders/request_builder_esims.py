from enum import Enum
from core import APP_URL, EndpointKeys
from request_builders.request_builder_main import BaseController


class EsimEndpoints(Enum):
    LIST_ESIMS = ("GET", f"{APP_URL}/sims", EndpointKeys.LIST_ESIMS.value)

    def __init__(self, method, path, key):
        self.method = method
        self.path = path
        self.key = key


class EsimController(BaseController):
    endpoints_enum = EsimEndpoints
