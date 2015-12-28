# -*- coding: utf-8 -*-

from seer import *


class DNS(Seer):
    def __init__(self, api_token, host=HOST, version=API_VERSION):
        Seer.__init__(self, api_token, host, version)

    def domain(self, domain, auto_retry=False):
        """Get ip from domain

            :param domain: domain name
            :type  domain: str
            :param auto_retry: Retry until success
            :type  auto_retry: Boolean

            :returns: dict -- result
            :raises:  APIError

        """
        self.body = dict(
            domain = domain
        )
        interface = '/dns/domain'
        response = self.request(interface, self.body, self.headers, auto_retry)
        result = response.json()

        return result

    def ip(self, ip, auto_retry=False):
        """Get domain by ip

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
        interface = '/dns/ip'
        response = self.request(interface, self.body, self.headers, auto_retry)
        result = response.json()

        return result
