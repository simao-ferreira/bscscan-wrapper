from bsc.module.enum.fields_enum import FieldsEnum as fields
from bsc.module.enum.paramters_enum import ParametersEnum as params
from bsc.module.module import Module


class Account(Module):

    def set_module_parameters(self):
        """Set url parameters for account module"""
        self.url_builder.set_parameters(params.MODULE, fields.ACCOUNT)

    def get_balance(self, address):
        """Get BNB balance of given address"""
        self.set_module_parameters()
        self.url_builder.set_parameters(params.ADDRESS, address)
        self.url_builder.set_parameters(params.ACTION, fields.BALANCE)
        self.url_builder.set_parameters(params.TAG, fields.LATEST)
        print(address)
        url = self.url_builder.build_url()

        response = self.connect(url)
        return response['result']

    def get_all_transactions(self):
        """ WIP """
        self.set_module_parameters()
        self.url_builder.set_parameters(params.ACTION, fields.TXLIST)
        self.url_builder.set_parameters(params.SORT, fields.ASC)
        url = self.url_builder.build_url()

        response = self.connect(url)
        return response

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
