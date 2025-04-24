"""
LeetCode Problem: 1399. Count Largest Group
Link: https://leetcode.com/problems/count-largest-group/
Difficulty: Easy
Topics: Hash Table
"""


def countLargestGroup(n: int) -> int:
    digits_sum = {}

    for i in range(1, n + 1):
        total = 0
        for digit in str(i):
            total += int(digit)
        digits_sum[total] = digits_sum.get(total, 0) + 1

    max_size = 0
    total_in_max_size = 0

    for i, digits in digits_sum.items():
        if digits > max_size:
            max_size = digits
            total_in_max_size = 1
        elif digits == max_size:
            total_in_max_size += 1

    return total_in_max_size


print(countLargestGroup(13) == 4)
