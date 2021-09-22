from bsc.enums.fields_enum import FieldsEnum as fields
from bsc.enums.paramters_enum import ParametersEnum as params
from bsc.modules.client import Client
from bsc.service.operations import in_BNB


class Account(Client):

    def __init__(self, address, api_key):
        Client.__init__(self, api_key)
        self.set_module_parameters(address)

    def set_module_parameters(self, address):
        """Set url parameters for account module"""
        self.set_request_parameters(params.ADDRESS, address)
        self.set_request_parameters(params.MODULE, fields.ACCOUNT)

    def get_balance(self):
        """Get BNB balance of given address"""
        self.set_request_parameters(params.ACTION, fields.BALANCE)
        self.set_request_parameters(params.TAG, fields.LATEST)
        self.build_url()

        request = self.connect()
        balance = f"BNB balance = {in_BNB(request['result'])}"
        return balance

    def get_all_transactions(self):
        """ WIP """
        self.set_request_parameters(params.ACTION, fields.TXLIST)
        self.set_request_parameters(params.SORT, fields.ASC)
        self.build_url()

        request = self.connect()
        return request

    def get_total_gas_spent(self):
        """
        WIP
        cumulativeGasUsed is the sum of gasUsed by this transaction and all preceding transactions in the same block.
        :return:
        """
        transactions = self.get_all_transactions()['result']
        # print(transactions)
        for tx in transactions:
            # print(tx)
            if tx['blockNumber'] == '10660239':
                print(tx)

    def get_latest_block(self):
        pass
