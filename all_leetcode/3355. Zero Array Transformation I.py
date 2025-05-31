"""
LeetCode Problem: 3335. Total Characters in String After Transformations I
Link: https://leetcode.com/problems/zero-array-transformation-i/
Difficulty: Medium
Topics: 1D Dynamic Programming, String
"""

from typing import List


def isZeroArray(nums: List[int], queries: List[List[int]]) -> bool:
    # 1. set up n and a changeArray that is size n + 1
    n = len(nums)
    changeArray = [0] * (n + 1)

    # 2. go thru each query, increment the left index of the query by 1, and decrement the right + 1 index of the query by 1. The reason we decrement right + 1 by 1 is because the array is unchanged at this point, since we'll eventually do prefixSum for each index, decrementing by 1 cancels out the incrementing by 1 we did at the start of the query
    for left, right in queries:
        changeArray[left] += 1
        changeArray[right + 1] -= 1

    # 3. for each i in range(n), check to see if you can decrement the value in nums[i] to 0, and as you view the indices, for i > 0, changeArray[i] is the prefixSum up to that point
    for i in range(n):
        if i > 0:
            changeArray[i] += changeArray[i - 1]
        if nums[i] > changeArray[i]:
            return False

    # 4. return True at the end if you never returned False
    return True


print(isZeroArray(nums=[1, 0, 1], queries=[[0, 2]]))
