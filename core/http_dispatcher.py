import pytest
import requests


def http_request(method, url, headers=None, json=None):
    return requests.request(method=method, url=url, headers=headers, json=json)
