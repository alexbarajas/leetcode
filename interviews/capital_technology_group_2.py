"""
Determine the factors of a number and then return the pth element of the list, sorted ascending. if there is no pth element, return 0
"""


def pthFactor(n, p):
    possible_factors = []

    for num in range(1, int(n ** 0.5) + 1):
        if n % num == 0:
            possible_factors.append(num)
            possible_factors.append(n // num)

    return sorted(possible_factors)[p - 1]


print(pthFactor(20, 3) == 4)
