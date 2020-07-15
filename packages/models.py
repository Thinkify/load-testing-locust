"""
    Defines the API request models
"""

import yaml


class RequestModel:
    """
    Loads the requests description from the specified data file and sets
    type, endpoint, body and headers for an API
    """

    def __init__(self, endpoint_name):
        self.__request_name = endpoint_name

        with open('data//requests.yaml') as file:
            self.__requests = yaml.safe_load(file)['REQUESTS_DESCRIPTION']

        self._type = self.__requests[self.__request_name]['TYPE']
        self._endpoint = self.__requests[self.__request_name]['ENDPOINT']
        self._body = self.__requests[self.__request_name]['BODY']
        self._headers = self.__requests[self.__request_name]['HEADERS']

    @property
    def type(self):
        """
        type of HTTP method
        Returns HTTP method type specified in data file
        -------
        """
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def endpoint(self):
        """
        Endpoint of API request
        Returns endpoint specified in data file
        -------
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, value):
        self._endpoint = value

    @property
    def body(self):
        """
        Body of API request
        Returns body specified in data file
        -------
        """
        return self._body

    @body.setter
    def body(self, value):
        self._body = value

    @property
    def headers(self):
        """
        Headers of API request
        Returns headers specified in data file
        -------
        """
        return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value
