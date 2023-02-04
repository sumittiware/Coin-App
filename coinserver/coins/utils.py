from _decimal import Decimal


def format_currency(amount, decimal_places=2, is_currency=True):
    amount = Decimal(amount)
    result = "$ " if is_currency else ""
    if amount >= 1000000000:
        return result + "{:,.{}f}b".format(amount / 1000000000, decimal_places)
    elif amount >= 1000000:
        return result + "{:,.{}f}m".format(amount / 1000000, decimal_places)
    elif amount >= 1000:
        return result + "{:,.{}f}k".format(amount / 1000, decimal_places)
    else:
        return result + "{:,.{}f}".format(amount, decimal_places)