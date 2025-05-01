"""
LeetCode Problem: 2962. Count Subarrays Where Max Element Appears at Least K Times
Link: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
Difficulty: Medium
Topics: Array, Sliding Window
"""

from typing import List


def countSubarrays(nums: List[int], k: int) -> int:
    # 1. set up n, the answer variable, get the high from nums and set the count of that high as 0 for now
    n = len(nums)
    answer = 0
    high = max(nums)
    count = 0

    # 2. using a left variable and a right value that moves as part of a for loop, use sliding window
    left = 0
    for right in range(n):
        # 2.1. if nums[right] == high, increase the count
        count += nums[right] == high
        # 2.2. for each iteration of right...
        while count == k:
            # 2.2.1. as long as count >= k, increase the answer by (n - right), this is because if you currently have a subarray that works, adding any number to the right of that subarray will work as well
            answer += n - right
            # 2.2.2. after you add to the answer, subtract 1 from the count if nums[left] == high because left will get shifted
            count -= nums[left] == high
            # 2.2.3. shift left
            left += 1

    # 3. return the answer
    return answer


print(countSubarrays(nums=[1, 3, 2, 3, 3], k=2) == 6)
