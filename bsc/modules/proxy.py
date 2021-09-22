from bsc.enums.fields_enum import FieldsEnum as fields
from bsc.enums.paramters_enum import ParametersEnum as params
from bsc.modules.client import Client
from bsc.service.operations import in_BNB


class Proxy(Client):

    def __init__(self, api_key):
        Client.__init__(self, api_key)
        self.set_module_parameters()

    def set_module_parameters(self):
        """Set url parameters for proxy module"""
        self.set_request_parameters(params.MODULE, fields.PROXY)

    def get_current_gas_price(self):
        """
        Get gas price
        manipulated object is in hexadecimal
        "result":"0x430e23400"
        """
        self.set_request_parameters(params.ACTION, fields.GAS_PRICE)
        self.build_url()

        request = self.connect()
        result = request['result']
        price = f"Current gas price in gwei = {int(result, 16)}, in BNB = {in_BNB(request['result'])}"
        return price
