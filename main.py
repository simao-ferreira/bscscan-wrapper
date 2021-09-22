from bsc.config.configuration import ADDRESS, API_KEY
from bsc.modules.accounts import Account
from bsc.modules.proxy import Proxy

if __name__ == '__main__':
    account = Account(ADDRESS, API_KEY)
    balance = account.get_balance()
    print(balance)

    # transactions = api.get_all_transactions()
    # print(transactions)

    # fees = api.get_total_gas_spent()
    # print(fees)

    proxy = Proxy(API_KEY)
    gas = proxy.get_current_gas_price()
    print(gas)
