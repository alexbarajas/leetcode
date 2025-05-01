"""
LeetCode Problem: 367. Valid Perfect Square
Link: https://leetcode.com/problems/valid-perfect-square/
Difficulty: Easy
Topics: Binary Search, Math
"""


def isPerfectSquare(num: int) -> bool:
    # # SOLUTION 1: understand it
    # high = int(num ** 0.5)
    # for i in range(high, high + 1):
    #     if i ** 2 == num:
    #         return True

    # return False

    # # SOLUTION 2: more efficient
    # return int(num ** 0.5) == num ** 0.5

    # SOLUTION 3: binary search
    if num < 2:
        return True

    left = 2
    right = num // 2

    while left <= right:
        midpoint = (right - left) // 2 + left
        current = midpoint * midpoint
        if current == num:
            return True
        elif current > num:
            right = midpoint - 1
        else:
            left = midpoint + 1

    return False


print(isPerfectSquare(16))
print(not isPerfectSquare(14))
