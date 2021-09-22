from bsc.module.enum.fields_enum import FieldsEnum as fields
from bsc.module.enum.paramters_enum import ParametersEnum as params
from bsc.module.module import Module


class Proxy(Module):

    def set_module_parameters(self):
        """Set url parameters for proxy module"""
        self.url_builder.set_parameters(params.MODULE, fields.PROXY)

    def get_current_gas_price(self):
        """
        Get gas price
        manipulated object is in hexadecimal
        "result":"0x430e23400"
        """
        self.set_module_parameters()
        self.url_builder.set_parameters(params.ACTION, fields.GAS_PRICE)
        url = self.url_builder.build_url()

        request = self.connect(url)
        return request['result']
