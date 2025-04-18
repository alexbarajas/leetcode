from typing import List


def maxCount(banned: List[int], n: int, maxSum: int) -> int:
    # SOLUTION 1: sets numbers_used as a variable
    # banned = set(banned)

    # current = 1
    # total = 0
    # numbers_used = 0

    # while total <= maxSum and current <= n:
    #     if current not in banned:
    #         total += current
    #         numbers_used += 1
    #     current += 1

    # return numbers_used if total < maxSum else numbers_used - 1

    # SOLUTION 2: sets numbers_used as a set and is more efficient on the site for some reason
    banned = set(banned)

    value = 1
    total = 0
    numbers = set()

    while total <= maxSum and value <= n:
        if value not in banned:
            total += value
            numbers.add(value)
        value += 1

    return len(numbers) if total < maxSum else len(numbers) - 1


print(maxCount(banned=[1, 6, 5], n=5, maxSum=6) == 2)
print(maxCount(banned=[11], n=7, maxSum=50) == 7)
