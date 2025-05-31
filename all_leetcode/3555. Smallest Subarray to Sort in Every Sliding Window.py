"""
LeetCode Problem: 3555. Smallest Subarray to Sort in Every Sliding Window
Link: https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/
Difficulty: Medium
Topics: Array, Two Pointers, Greedy
Description: You are given an integer array nums and an integer k.

For each contiguous subarray of length k, determine the minimum length of a continuous segment that must be sorted so that the entire window becomes non‑decreasing; if the window is already sorted, its required length is zero.

Return an array of length n − k + 1 where each element corresponds to the answer for its window.
"""

from typing import List


def minSubarraySort(nums: List[int], k: int) -> List[int]:
    # 1. set up n and the answer array
    n = len(nums)
    answer = []

    # 2. for every i in range(n - k + 1), make a window using the given i with size k, and also make a sorted_window that has those numbers from the window array, except in sorted order
    for i in range(n - k + 1):
        window = nums[i: i + k]
        sorted_window = sorted(window)

        # 2.1. find the leftmost position where the elements differ
        start = 0
        while start < k and window[start] == sorted_window[start]:
            start += 1

        # 2.2. find the rightmost position where the elements differ
        end = k - 1
        while end >= 0 and window[end] == sorted_window[end]:
            end -= 1

        # 2.3. append the length of the subarray that needs to be sorted to make the window sorted, or 0 if it's already sorted
        answer.append(end - start + 1 if start <= end else 0)

    # 3. return the answer at the end
    return answer


print(minSubarraySort(nums=[1, 3, 2, 4, 5], k=3) == [2, 2, 0])
print(minSubarraySort(nums=[5, 4, 3, 2, 1], k=4) == [4, 4])
