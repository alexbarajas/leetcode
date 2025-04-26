"""
LeetCode Problem: 78. Subsets
Link: https://leetcode.com/problems/subsets/
Difficulty: Medium
Topics: Array, Backtracking
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    # 1. set up an empty array of arrays
    answer = [[]]

    # 2. go thru each num in nums, and add to the previous arrays in answer for each num
    for num in nums:
        answer += [previous + [num] for previous in answer]

    # 3. return the answer array
    return answer


def subsets2(nums: List[int]) -> List[List[int]]:
    answer = [[]]

    for num in nums:
        for i in range(len(answer)):
            answer += [answer[i] + [num]]

    return answer


print(subsets([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
print(subsets2([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
