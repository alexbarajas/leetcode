"""
LeetCode Problem: 198. House Robber
Link: https://leetcode.com/problems/house-robber/
Difficulty: Medium
Topics: Array, 1D Dynamic Programming
"""

from typing import List


def rob(nums: List[int]) -> int:
    # 0. base case, if len(nums) <= 2, then return max(nums)
    n = len(nums)
    if n <= 2:
        return max(nums)

    # 1. set up a houses array with a 0 for each index in nums
    houses = [0 for i in range(n)]

    # 2. go thru i in range(len(nums)), if i == 0, set houses[i] equal to nums[i], for the rest of the i's, get the max of the houses value before it, or the ith nums value plus the (ith - 2) houses value
    for i in range(n):
        if i == 0:
            houses[i] = nums[i]
        else:
            houses[i] = max(houses[i - 1], nums[i] + houses[i - 2])

    # 3. return the last value in the houses array
    # print(houses)
    return houses[-1]


print(rob([1, 2, 3, 1]) == 4)
