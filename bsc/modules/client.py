import collections

import requests

from bsc.enums.paramters_enum import ParametersEnum as params


class Client(object):

    def __init__(self):
        self.http = requests.session()
        self.url_parameters = {}
        self.url = None

    def build_url(self):
        parameters = [key + val if val else '' for key, val in self.url_parameters.items()]
        self.url = params.BSC_URL + ''.join(parameters)

    def connect(self):
        try:
            # print(self.url)
            request = self.http.get(self.url)
        except requests.exceptions.ConnectionError:
            raise Exception

        if request.status_code == 200:
            response = request.json()
            if response.get('status') == '1':
                return response
            else:
                raise Exception(response.get('message', 'No message was found!'))
        else:
            print("Response status: %s" % request.status_code)

    def build_url_parameters(self, address, api_key):
        self.url_parameters = collections.OrderedDict([
            (params.MODULE, ''),
            (params.ADDRESS, address),
            (params.ACTION, ''),
            (params.SORT, ''),
            (params.START_BLOCK, ''),
            (params.END_BLOCK, ''),
            (params.TAG, ''),
            (params.API_KEY, api_key)
        ])
