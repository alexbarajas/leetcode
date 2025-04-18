
"""
Q4 - Clean Prices
=================

Summary
-------
Write a function that takes an iterator of "dirty" price data and yields an
iterator of "clean" price data (via yield).  The input iterator provides a
stream of tuples consisting of a integer timestamp and a price.  The timestamps
will increase by a fixed interval.  The data may be dirty: bad timestamps
(i.e. not a multiple of the interval), missing prices or duplicate timestamp/prices.

Clean the stream by inserting price points (with price=None) where price points
are missing and removing duplicate price points (keep the first price).
Ensuring the timestamps they are in increasing timestamp order with a fixed
interval.

You can assume the first (time,price) input tuple is valid.  Using the `yeild`
keyword will make the clean_prices function into an generator (returns an iterator).
Timestamps will always be positive numbers and greater than zero.

Inputs
------
values - an iterator that returns a stream two element (time, price) tuples
interval - the interval every timestamp in values should increase by

Returns
-------
An iterator that generates a cleaned stream of two-element tuples where the
timestamps increase by the input increment.  If the timstamp did not exist in
the input, the price should be None.  If duplicate timestamps were in the input
iterator, use the first price with the same timestamp as the price.


Examples
--------
Inputs:
    values   = iter([(12, 1.2), (14, 1.3), (18, 1.4)])
    interval = 2

Return:
    iter([(12, 1.2), (14, 1.3), (16, None), (18, 1.4)])


Inputs:
    values   = iter([(28, 1.4), (31, 1.5), (31, 1.4), (34, 1.3)])
    interval = 3

Return:
    iter([(28, 1.4), (31, 1.5), (34, 1.3)]


Inputs:
    values   = iter([(10, 1.3), (2, 1.4), (14, 1.4), (14, 1.3), (26, 1.2), (18, 1.3)])
    interval = 4

Return:
    iter([(10, 1.3), (14, 1.4), (18, None), (22, None), (26, 1.2)])


"""

def clean_prices(prices:iter, interval:int) -> iter:
    pass


values   = iter([(12, 1.2), (14, 1.3), (18, 1.4)])
interval = 2

print(clean_prices(values, interval))