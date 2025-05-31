"""
LeetCode Problem: 1920. Build Array from Permutation
Link: https://leetcode.com/problems/build-array-from-permutation/
Difficulty: Easy
Topics: Array
"""

from typing import List


def buildArray(nums: List[int]) -> List[int]:
    # # SOLUTION 1: iterative
    # # REDO: https://leetcode.com/problems/build-array-from-permutation/solutions/1315926/python-o-n-time-o-1-space-w-full-explanation/
    # n = len(nums)

    # for i in range(n):
    #     nums[i] += n * (nums[nums[i]] % n)
    # for i in range(n):
    #     nums[i] //= n

    # return nums

    # SOLUTION 2: one line
    return [nums[nums[i]] for i in range(len(nums))]


print(buildArray([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3])
