"""
LeetCode Problem: 215. Kth Largest Element in an Array
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Difficulty: Medium
Topics: Array, Heap, Sorting
"""

import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    # SOLUTION 1: easiest to do
    # 1. set up a heap
    heap = []

    # 2. heappush every number into the heap
    for number in nums:
        heapq.heappush(heap, number)

    # 3. get the k nlargest values from the heap, and return the last value in that array
    return heapq.nlargest(k, heap)[-1]

    # # SOLUTION 2: can also use nsmallest and negative numbers
    # for num in nums:
    #     heapq.heappush(heap, -num)
    #
    # return -heapq.nsmallest(k, heap)[-1]

    # # SOLUTION 3: most efficient
    # k = len(nums) - k
    #
    # def quickSelect(left, right):
    #     # quickSelect(0, len(nums) - 1)
    #     # pivot = 4
    #     # pointer = 0
    #     # left = 0
    #     # right = 5
    #     # i = 0
    #     # k = 4
    #     # [3, 2, 1, 5, 6, 4] turns into
    #     # pivot = 4
    #     # pointer = 3
    #     # left = 0
    #     # right = 5
    #     # i = 4
    #     # k = 4
    #     # [3, 2, 1, 4, 6, 5], pointer < k, so
    #     # quickSelect(4, 5)
    #     # pivot = 5
    #     # pointer = 4
    #     # left = 4
    #     # right = 5
    #     # i = 4
    #     # [3, 2, 1, 4, 6, 5] turns into
    #     # pivot = 5
    #     # pointer = 4
    #     # left = 4
    #     # right = 5
    #     # i = 4
    #     # [3, 2, 1, 4, 5, 6]
    #     # pointer and k are both 4, so return nums[pointer], which is 5
    #     pivot = nums[right]
    #     pointer = left
    #     for i in range(left, right):
    #         if nums[i] <= pivot:
    #             nums[pointer], nums[i] = nums[i], nums[pointer]
    #             pointer += 1
    #     nums[pointer], nums[right] = pivot, nums[pointer]
    #     # print(pivot, pointer, left, right, i, k, nums)
    #
    #     if pointer > k:
    #         return quickSelect(left, pointer - 1)
    #     elif pointer < k:
    #         return quickSelect(pointer + 1, right)
    #     else:
    #         return nums[pointer]
    #
    # return quickSelect(0, len(nums) - 1)


print(findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2) == 5)
print(findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4)
