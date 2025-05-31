"""
LeetCode Problem: 945. Minimum Increment to Make Array Unique
Link: https://leetcode.com/problems/minimum-increment-to-make-array-unique/
Difficulty: Medium
Topics: Array, Greedy
"""

from typing import List


def minIncrementForUnique(nums: List[int]) -> int:
    answer = 0
    nums.sort()

    for i in range(1, len(nums)):
        previous = nums[i - 1]
        if nums[i] <= previous:
            answer += previous + 1 - nums[i]
            nums[i] = previous + 1

    return answer


print(minIncrementForUnique([1, 2, 2]) == 1)
print(minIncrementForUnique([3, 2, 1, 2, 1, 7]) == 6)
