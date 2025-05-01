"""
LeetCode Problem: 217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Topics: Hash Table
"""

from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False


print(containsDuplicate([1, 2, 3, 1]))
print(not containsDuplicate([1, 2, 3, 4]))
