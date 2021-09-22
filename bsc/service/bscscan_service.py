from bsc.config.configuration import ADDRESS
from bsc.module.account import Account
from bsc.module.proxy import Proxy
from bsc.service.operations import in_BNB, in_gwei


class BscscanService:

    def __init__(self):
        self.proxy = Proxy()
        self.account = Account()

    def current_gas_price(self) -> str:
        """
        get current gas prices (Gwei/Bnb)
        """
        result = self.proxy.get_current_gas_price()
        price = f"Current gas price in gwei = {in_gwei(result)}, in BNB = {in_BNB(result)}"
        return price

    def current_balance(self):
        """
        get current gas prices (Gwei/Bnb)
        """
        result = self.account.get_balance(ADDRESS)
        balance = f"BNB balance = {in_BNB(result)}"
        return balance
