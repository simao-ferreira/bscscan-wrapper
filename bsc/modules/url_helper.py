import collections

from bsc.enums.paramters_enum import ParametersEnum as params


class UrlBuilder:

    def __init__(self, api_key):
        self.url = None
        self.url_parameters = collections.OrderedDict([
            (params.MODULE, ''),
            (params.ADDRESS, ''),
            (params.ACTION, ''),
            (params.SORT, ''),
            (params.START_BLOCK, ''),
            (params.END_BLOCK, ''),
            (params.TAG, ''),
            (params.API_KEY, api_key)
        ])

    def set_request_parameters(self, key, value):
        self.url_parameters[key] = value

    def build_url(self):
        parameters = [key + val if val else '' for key, val in self.url_parameters.items()]
        self.url = params.BSC_URL + ''.join(parameters)
