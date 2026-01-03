python
import requests

class ApiClient:

    @staticmethod
    def post(url, headers, payload):
        return requests.post(url, json=payload, headers=headers)

    @staticmethod
    def get(url, headers):
        return requests.get(url, headers=headers)
