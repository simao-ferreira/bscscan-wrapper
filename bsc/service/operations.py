import decimal
import re


def convert_gwei_to_BNB(value) -> decimal.Decimal:
    """
    Conversion from gwei to BNB
    where 1 BNB = 10^18 gwei
    according to https://bscscan.com/unitconverter
    """
    return int(value) / 10 ** 18


def is_hex(value) -> decimal.Decimal:
    """
    Evaluate if hexadecimal according to jsonrpc defined response
        0x[values]
    :param value: 0x430e23400
    :return: True
    """
    return re.fullmatch(r"0x[0-9A-Fa-f]+", value or "") is not None


def in_BNB(value) -> decimal.Decimal:
    """
    Convert gwei to BNB, source value can be decimal or hexadecimal
    :param value: 0x430e23400
    :return: 0.000000018
    """
    if is_hex(value):
        amount = int(value, 16)
        return convert_gwei_to_BNB(amount)
    else:
        return convert_gwei_to_BNB(value)
