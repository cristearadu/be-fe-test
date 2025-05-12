from enum import Enum
from core import APP_URL, EndpointKeys
from request_builders.request_builder_main import BaseController


class PackageEndpoints(Enum):
    GET_PACKAGES = ("GET", f"{APP_URL}/packages", EndpointKeys.GET_PACKAGES.value)

    def __init__(self, method, path, key):
        self.method = method
        self.path = path
        self.key = key


class PackageController(BaseController):
    endpoints_enum = PackageEndpoints
