import os
from enum import Enum
from dotenv import load_dotenv

load_dotenv()

API_VERSION = os.getenv('API_VERSION')
APP_URL = f"{os.getenv('BASE_URL')}/{API_VERSION}"
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TOKEN_URL = f"{APP_URL}/oauth/token"
ORDER_URL = f"{APP_URL}/orders"
ESIM_LIST_URL = f"{APP_URL}/esims"
PACKAGE_SLUG = "merhaba-7days-1gb"
ROOT_WORKING_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_FOLDER = 'output'
DEFAULT_SIM_TYPE = 'sim'
DEFAULT_APN_VALUE = 'airalo2'
ORDER_STATUS = 'order.status'

class EndpointKeys(str, Enum):
    CREATE_ORDER = "create_order"
    LIST_ESIMS = "list_esims"
    GET_PACKAGES = "get_packages"
    AUTH_TOKEN = "auth_token"


class HTTPStatusCodes(Enum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    TOO_MANY_REQUESTS = 429
    INTERNAL_SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 503


class GrantType(Enum):
    client_credentials = 'client_credentials'
