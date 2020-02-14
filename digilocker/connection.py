import requests
import json

from digilocker.exceptions import TokenExpiredException, RateLimitException


class Connection(object):
    def __init__(self):
        self._session = requests.Session()
        self._session.headers = {
            "Accept": "application/json"
        }

    def make_request(self, r_url, method, data=None, headers=None):
        if not data:
            data = dict()

        if headers:
            for header_name, header_value in headers.items():
                self._session.headers.update({header_name: header_value})

        response = self._session.request(
            method=method, url=r_url, data=json.dumps(data)
        )
        return self.process_response(response)

    @staticmethod
    def process_response(response):
        """
            Method to process the responses from the digilocker.
        :param response: (object)
        :return:
        """
        result = dict()
        if response.status_code in [200, 201, 202]:
            result = response.json()
        elif response.status_code == 401:
            raise TokenExpiredException("Token expired")
        elif response.status_code == 429:
            raise RateLimitException("Rate limit :{}".format(response.text))
        else:
            raise ValueError("Error while fetching : {}".format(response.text))
        return result
