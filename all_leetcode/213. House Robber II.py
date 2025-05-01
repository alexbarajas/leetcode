"""
LeetCode Problem: 213. House Robber II
Link: https://leetcode.com/problems/house-robber-ii/
Difficulty: Medium
Topics: Array, 1D Dynamic Programming
"""

from typing import List


def rob(nums: List[int]) -> int:
    # 0. base case, if nums has less than 4 numbers, return the max num
    if len(nums) < 4:
        return max(nums)

    # 1. make a function to find the max_profit of an array based on the house robbing criteria
    def max_profit(nums):
        # 1.1. set a houses array with 0 for each num in nums
        houses = [0 for i in range(len(nums))]
        # 1.2. go thru the array, applying the house robbing criteria
        for i in range(len(nums)):
            # 1.2.1. the first value in houses is equal to the first value in nums
            if i == 0:
                houses[i] = nums[i]
            # 1.2.2. the other values in houses are the max of houses[1 - 1], or houses[i - 2] + nums[i]
            else:
                houses[i] = max(houses[i - 1], houses[i - 2] + nums[i])
        # 1.3. return the last value in houses
        return houses[-1]

    # 2. initialize the max_profit function for nums[1:], and nums[:-1], return the max of these functions
    return max(max_profit(nums[1:]), max_profit(nums[:-1]))


print(rob([2, 3, 2]) == 3)
print(rob([1, 2, 3, 1]) == 4)
