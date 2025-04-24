"""
LeetCode Problem: 2799. Count Complete Subarrays in an Array
Link: https://leetcode.com/problems/count-complete-subarrays-in-an-array/
Difficulty: Medium
Topics: Array, Sliding Window
"""

from typing import List


def countCompleteSubarrays(nums: List[int]) -> int:
    n = len(nums)
    distinct = len(set(nums))
    hashmap = {}
    answer = 0

    left = 0
    for right in range(n):
        hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1

        while len(hashmap) == distinct:
            # print(right)
            # print(nums[left: right + 1])
            answer += n - right  # we increment the answer by n - right each time we find a complete subarray, this is because when you find a complete subarray ending at position "right", "n - right" counts all possible ways to extend that subarray to the right while still keeping all distinct elements
            hashmap[nums[left]] -= 1
            if hashmap[nums[left]] == 0:
                hashmap.pop(nums[left])
            left += 1

    return answer


print(countCompleteSubarrays([1, 3, 1, 2, 2]) == 4)
print(countCompleteSubarrays([5, 5, 5, 5]) == 10)
