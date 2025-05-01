"""
LeetCode Problem: 442. Find All Duplicates in an Array
Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
Difficulty: Medium
Topics: Hash Table, Array
"""

from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    # SOLUTION 1: simple hashset solution
    # hashset = set()
    # answer = []
    # for number in nums:
    #     if number not in hashset:
    #         hashset.add(number)
    #     else:
    #         answer.append(number)
    # return answer

    # SOLUTION 2: better solution changing nums in place
    # 1. set up an empty answer array
    answer = []

    # 2. go thru the nums array, and mark every value you see using the nums array itself and making the seen numbers negative. if the number is already negative, then that means it has already been seen, so append it to the answer array.
    for num in nums:
        value = abs(num)
        if nums[value - 1] > 0:  # not seen before
            nums[value - 1] *= -1
        else:  # seen before since it's been turned to its negative value
            answer.append(value)

    # 3. return the answer array
    return answer


print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3])
print(findDuplicates([1]) == [])
