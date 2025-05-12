from core import http_request


class BaseController:
    endpoints_enum = None

    def request(self, key, headers=None, payload=None, **kwargs):
        if not self.endpoints_enum:
            raise NotImplementedError("You must define 'endpoints_enum' in subclass")

        endpoint = next((e for e in self.endpoints_enum if e.key == key), None)
        if not endpoint:
            raise ValueError(f"Unknown endpoint key: {key}")

        formatted_url = endpoint.path.format(**kwargs)
        return http_request(endpoint.method, formatted_url, headers=headers, json=payload)
