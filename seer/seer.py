# -*- coding: utf-8 -*-

from json import dumps

import requests


# Defaults.
HOST = 'http://seer.intra.nsfocus.com:8000/api'
API_VERSION = 1


# Exception Definition.
class APIError(Exception):
    pass


# Base Class
class Seer(object):
    """The base class.
    """

    def __init__(self, api_token, host=HOST, api_version=API_VERSION):
        self.host = host
        self.api_version = api_version
        self.api_token = api_token
        self.headers = {
            "Accept": "application/seer+json;version=%d" % self.api_version,
            "Content-Type": "application/json",
            "X-SEER-TOKEN": api_token
        }
        self.body = dict()
        self.method = 'POST'

    def request(self, interface, body, header, auto_retry=False):
        """Send request to SEER API.

            :param interface: api interface
            :type  interface: str
            :param auto_retry: Retry until success
            :type  auto_retry: Boolean

            :returns: dict -- result
            :raises:  APIError

        """

        request_url = self.host + interface
        response = None

        while True:
            try:
                if self.method == 'POST':
                    json_data = dumps(body)
                    response = requests.post(request_url, headers=header, data=json_data)
                else:
                    response = requests.get(request_url, headers=self.headers)

                if response is not None:
                    return response

            except requests.exceptions.Timeout:
                if auto_retry:
                    continue
                else:
                    break
            except requests.exceptions.ConnectionError as e:
                break
            except requests.exceptions.HTTPError as e:
                break

        raise APIError()
