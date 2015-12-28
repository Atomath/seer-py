# -*- coding: utf-8 -*-

from seer import *


class Org(Seer):
    def __init__(self, api_token, host=HOST, version=API_VERSION):
        Seer.__init__(self, api_token, host, version)

    def ip(self, ip, auto_retry=False):
        """Get Organization by ip

            :param ip: IP address
            :type  ip: str
            :param auto_retry: Retry until success
            :type  auto_retry: Boolean

            :returns: dict -- result
            :raises:  APIError

        """

        self.body = dict(
            ip = ip
        )
        interface = '/org/ip'
        response = self.request(interface, self.body, self.headers, auto_retry)
        result = response.json()

        return result

    def asn(self, asn, auto_retry=False):
        """Get Organization by AS number

            :param asn: AS number
            :type  asn: int
            :param auto_retry: Retry until success
            :type  auto_retry: Boolean

            :returns: dict -- result
            :raises:  APIError

        """

        self.body = dict(
            asn = asn
        )
        interface = '/org/asn'
        response = self.request(interface, self.body, self.headers, auto_retry)
        result = response.json()

        return result
