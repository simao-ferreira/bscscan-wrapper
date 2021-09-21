from bsc.enums.paramters_enum import ParametersEnum as params
from bsc.modules.client import Client


class Account(Client):

    def __init__(self, address, api_key):
        Client.__init__(self)
        self.set_module_parameters(address, api_key)

    def set_module_parameters(self, address, api_key):
        """Set url parameters for account module"""
        self.build_url_parameters(address, api_key)
        self.url_parameters[params.MODULE] = 'account'

    def get_balance(self):
        """Get BNB balance of given address"""
        self.url_parameters[params.ACTION] = 'balance'
        self.url_parameters[params.TAG] = 'latest'
        self.build_url()

        request = self.connect()
        balance = f"BNB balance = {self.convert_gwei_to_BNB(request['result'])}"
        return balance

    @staticmethod
    def convert_gwei_to_BNB(result):
        """
        Conversion from gwei to BNB
        where 1 BNB = 10^18 gwei
        according to https://bscscan.com/unitconverter
        """
        return int(result) / 10 ** 18
