# -*- coding: utf-8 -*-

from seer import *


class Hosts(Seer):
    def __init__(self, api_token, host=HOST, version=API_VERSION):
        Seer.__init__(self, api_token, host, version)

    def ip(self, ip, minify=False, auto_retry=False):
        """Get host by ip

            :param ip:  IP Address
            :type  ip: str
            :param minify: a customizable set of options
            :type  minify: Boolean
            :param auto_retry: Retry until success
            :type  auto_retry: Boolean

            :returns: dict -- result
            :raises:  APIError

        """

        self.body = dict(
            ip = ip,
            minify = minify
        )
        interface = '/hosts/ip'
        response = self.request(interface, self.body, self.headers, auto_retry)
        result = response.json()

        return result

    def port(self, port, page=1, minify=False, auto_retry=False):
        """Get host by port

            :param port:  port to search
            :type  port: int
            :param page: page number
            :type  page: int
            :param minify: a customizable set of options
            :type  minify: Boolean
            :param auto_retry: Retry until success
            :type  auto_retry: Boolean

            :returns: dict -- result
            :raises:  APIError

        """

        self.body = dict(
            port = port,
            minify = minify,
            page = page
        )
        interface = '/hosts/port'
        response = self.request(interface, self.body, self.headers, auto_retry)
        result = response.json()

        return result

    def service(self, service, page=1, minify=False, auto_retry=False):
        """Get host by service

            :param service:  service to search
            :type  service: str
            :param page: page number
            :type  page: int
            :param minify: a customizable set of options
            :type  minify: Boolean
            :param auto_retry: Retry until success
            :type  auto_retry: Boolean

            :returns: dict -- result
            :raises:  APIError

        """

        self.body = dict(
            service = service,
            minify = minify,
            page = page
        )
        interface = '/hosts/service'
        response = self.request(interface, self.body, self.headers, auto_retry)
        result = response.json()

        return result

    def aggs(self, query, fields, auto_retry=False):
        """Aggregations by query and field

            :param query:  Custom query
            :type  query: str
            :param fields: fields seperated by comma
            :type  fields: str
            :param auto_retry: Retry until success
            :type  auto_retry: Boolean

            :returns: dict -- result
            :raises:  APIError

        """

        self.body = dict(
            query = query,
            fields = fields,
        )
        interface = '/hosts/aggs'
        response = self.request(interface, self.body, self.headers, auto_retry)
        result = response.json()

        return result

    def search(self, query, page, minify, auto_retry=False):
        """Get hosts by custom search

            :param query: Custom query
            :type  query: str
            :param page: page number
            :type  page: int
            :param minify: a customizable set of options
            :type  minify: Boolean
            :param auto_retry: Retry until success
            :type  auto_retry: Boolean

            :returns: dict -- result
            :raises:  APIError

        """

        self.body = dict(
            query = query,
            minify = minify,
            page = page,
        )
        interface = '/hosts/search'
        response = self.request(interface, self.body, self.headers, auto_retry)
        result = response.json()

        return result
