"""
LeetCode Problem: 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros
Link: https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
Difficulty: Medium
Topics: Array, Greedy
"""

from typing import List


def minSum(nums1: List[int], nums2: List[int]) -> int:
    min1 = 0
    min2 = 0

    zero1 = False
    zero2 = False

    for num in nums1:
        min1 += num if num else 1
        if not num:
            zero1 = True

    for num in nums2:
        min2 += num if num else 1
        if not num:
            zero2 = True

    if (not zero2 and min1 > min2) or (not zero1 and min1 < min2):
        return -1

    return max(min1, min2)


print(minSum(nums1=[3, 2, 0, 1, 0], nums2=[6, 5, 0]) == 12)
