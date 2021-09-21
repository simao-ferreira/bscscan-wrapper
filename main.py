from bsc.config.configuration import ADDRESS, API_KEY
from bsc.modules.accounts import Account

if __name__ == '__main__':
    api = Account(ADDRESS, API_KEY)
    balance = api.get_balance()
    print(balance)
