from enum import Enum
from core import APP_URL, EndpointKeys
from request_builders.request_builder_main import BaseController


class AuthEndpoints(Enum):
    GET_TOKEN = ("POST", f"{APP_URL}/token", EndpointKeys.AUTH_TOKEN.value)

    def __init__(self, method, path, key):
        self.method = method
        self.path = path
        self.key = key


class AuthController(BaseController):
    endpoints_enum = AuthEndpoints
