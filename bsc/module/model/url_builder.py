import collections
import dataclasses

from bsc.config.configuration import API_KEY
from bsc.module.enum.paramters_enum import ParametersEnum as params


@dataclasses.dataclass
class UrlBuilder:

    def __init__(self):
        self.url_parameters = collections.OrderedDict([
            (params.MODULE, ''),
            (params.ADDRESS, ''),
            (params.ACTION, ''),
            (params.SORT, ''),
            (params.START_BLOCK, ''),
            (params.END_BLOCK, ''),
            (params.TAG, ''),
            (params.API_KEY, API_KEY)
        ])

    def set_parameters(self, key, value):
        self.url_parameters[key] = value

    def build_url(self):
        parameters = [key + val if val else '' for key, val in self.url_parameters.items()]
        return params.BSC_URL + ''.join(parameters)
