"""
LeetCode Problem: 3423. Maximum Difference Between Adjacent Elements in a Circular Array
Link: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
Difficulty: Easy
Topics: Array
Description: Given a circular array nums, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent.
"""

from typing import List


def maxAdjacentDistance(nums: List[int]) -> int:
    n = len(nums)
    answer = 0

    for i in range(n):
        answer = max(answer, abs(nums[i] - nums[(i + 1) % n]))

    return answer


print(maxAdjacentDistance([1, 2, 4]) == 3)
