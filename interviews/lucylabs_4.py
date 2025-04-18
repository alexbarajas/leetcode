"""
Q5 - Convert Currency
=====================

Summary
-------
Convert an amount in one currency (src_ccy) to the equivalent amount in another
currency (dst_ccy) using a dictionary of foreign exchange prices as the guide.

There may not be a direct conversion price for the input currencies's.  It may
be necessary to use an intermediary currency. example with the following prices:

    prices = {'JPY/USD': 100, 'CNY/JPY': 20}

To convert from USD to CNY, you would need to convert twice from USD -> JPY -> CNY.
For the purposes of this question, there will never be more than one intermediary
nor will there ever be more than one viable conversion path.

Inputs
------
amount  - the amount to convert (a float)
src_ccy - the source currency
dst_ccy - the target currency
prices  - a dict of prices where the keys are symbols such as "ccy0/ccy1" and the
          values are the price of ccy0 in ccy1 units.  For example, { "ABC/DEF": 2.0 }
          means that 1 ABC = 2 DEF and 1 DEF = 0.5 ABC.

Returns
-------
The amount in dst_ccy units.  If the amount cannot be converted, return None

Examples
--------
For all the following examples, assume:

    prices  = {'CNY/USD': 0.20, 'USD/JPY': 120.0, 'GBP/USD': 1.50, 'GBP/JPY': 180.0}

Inputs:
    amount  = 50.00
    src_ccy = 'CNY'
    dst_ccy = 'USD'
Return:
    10.0


Inputs:
    amount  = 6.00
    src_ccy = 'USD'
    dst_ccy = 'GBP'
Return:
    4.0


Inputs:
    amount  = 480.0
    src_ccy = 'JPY'
    dst_ccy = 'CNY'
Return:
    20.0


Inputs:
    amount  = 15.0
    src_ccy = 'CNY'
    dst_ccy = 'GBP'
Return:
    2.0


Inputs:
    amount  = 15.0
    src_ccy = 'CNY'
    dst_ccy = 'USD'
Return:
    3.0

"""


def convert_ccy(amount: float, src_ccy: str, dst_ccy: str, prices: dict) -> float:
    # 0. set up keys and their inverse and check if they are in prices to return the corresponding amount
    key = src_ccy + "/" + dst_ccy
    inversekey = dst_ccy + "/" + src_ccy
    if key in prices:
        return amount * prices[key]
    elif inversekey in prices:
        return amount * (1 / prices[inversekey])
    # 1. if you need to convert then make a newPrices hashset and insert the components of the conversions
    newPrices = set()
    for price in prices.keys():
        newPrices.add((price[:3], price[4:], prices[price]))
        newPrices.add((price[4:], price[:3], 1 / prices[price]))
    # 2. obtain the final conversion
    for src, dst, conv in newPrices:  # this is very inefficient, but I ran out of time before optimizing it
        if src == src_ccy:
            newsrc = dst
            newamount = conv
            for src, dst, conv in newPrices:
                if newsrc == src:
                    if dst == dst_ccy:
                        return amount * newamount * conv


prices = {'CNY/USD': 0.20, 'USD/JPY': 120.0, 'GBP/USD': 1.50, 'GBP/JPY': 180.0}

amount = 50.00
src_ccy = 'CNY'
dst_ccy = 'USD'

print(convert_ccy(amount, src_ccy, dst_ccy, prices))

amount = 6.00
src_ccy = 'USD'
dst_ccy = 'GBP'

print(convert_ccy(amount, src_ccy, dst_ccy, prices))

amount = 480.0
src_ccy = 'JPY'
dst_ccy = 'CNY'

print(convert_ccy(amount, src_ccy, dst_ccy, prices))

amount = 15.0
src_ccy = 'CNY'
dst_ccy = 'GBP'

print(convert_ccy(amount, src_ccy, dst_ccy, prices))

amount = 15.0
src_ccy = 'CNY'
dst_ccy = 'USD'

print(convert_ccy(amount, src_ccy, dst_ccy, prices))
