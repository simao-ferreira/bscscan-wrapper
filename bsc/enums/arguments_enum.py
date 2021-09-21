class ArgumentsEnum:
    BSC_URL: str = 'https://api.bscscan.com/api?'

    ACCOUNT: str = "account"
    BLOCK: str = "block"
    CONTRACT: str = "contract"
    GASTRACKER: str = "gastracker"
    LOGS: str = "logs"
    TOKEN: str = "token"
    TRANSACTION: str = "transaction"

    ACTION: str = "&action="
    ADDRESS: str = "&address="
    API_KEY: str = "&apikey="
    END_BLOCK: str = "&endblock="
    GAS_PRICE: str = "&gasPrice="
    GAS: str = "&gas="
    MODULE: str = "module="
    SORT: str = "&sort="
    START_BLOCK: str = "&startblock="
    TAG: str = "&tag="

    ASC: str = 'asc'
    BALANCE: str = "balance"
    LATEST: str = "latest"
    TXLIST_INTERNAL: str = "txlistinternal"
    TXLIST: str = "txlist"
