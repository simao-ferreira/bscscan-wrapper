from bsc.service.bscscan_service import BscscanService

if __name__ == '__main__':
    service = BscscanService()

    balance = service.current_balance()
    print(balance)

    # transactions = api.get_all_transactions()
    # print(transactions)

    # fees = api.get_total_gas_spent()
    # print(fees)

    gas = service.current_gas_price()
    print(gas)
