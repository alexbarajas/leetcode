"""
Q3 - Any Base
=============

Summary
-------
Write a function that returns a number's representations in an arbitrary base
using an arbitrary alphabet (a set of glpyhs).

To illustrate, the alphabet for base 8 would be "01234567" and for base 16 the
alphabet would be "01234567890ABCDEF".  For this question, the alphabet could
be any set of characters.  The first char will represent 0 (zero), the next
character 1, and so forth.  The base is implied by the number of characters in
the alphabet.

Inputs
------
n - an integer number to convert
alpha - string containing the alphabet (at least 2 chars)

Returns
-------
A string representation of the number in the base implied by the supplied
alphabet using the letters of the alphabet.

Examples
--------
Inputs:
    n = 5
    alpha = "01"

Return:
    101

Inputs:
    n = 11
    alpha = "abc"

Return:
    bac

Inputs:
    n = -33
    alpha = "#xyz"

Return:
    -y#x

"""


def any_base(n: int, alpha: str) -> str:
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % alpha))
        n //= alpha
    return digits[::-1]

n = 5
alpha = "01"

print(any_base(n, alpha))