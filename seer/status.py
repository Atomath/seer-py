# -*- coding: utf-8 -# -*- coding: utf-8 -*-

from seer import *


class Status(Seer):
    def __init__(self, api_token, host=HOST, version=API_VERSION):
        Seer.__init__(self, api_token, host, version)
        self.method = 'GET'

    def services(self, auto_retry=False):
        pass

    def ports(self, auto_retry=False):
        pass

    def token(self, auto_retry=False):
        """Get status of token

        :param auto_retry: Retry until success
        :type  auto_retry: Boolean

        :returns: dict -- result
        :raises:  APIError

        """
        interface = '/status/token'
        response = self.request(interface, None, self.headers, auto_retry)
        result = response.json()

        return result
