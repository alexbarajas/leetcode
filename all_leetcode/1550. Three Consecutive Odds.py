"""
LeetCode Problem: 1550. Three Consecutive Odds
Link: https://leetcode.com/problems/three-consecutive-odds/
Difficulty: Easy
Topics: Array
"""

from typing import List


def threeConsecutiveOdds(arr: List[int]) -> bool:
    # 1. set up a pointer
    pointer = 0

    # 2. set a loop while the pointer is less than len(arr) - 2
    while pointer < len(arr) - 2:
        # 2.1. if the pointer is odd, increment it by 1
        if arr[pointer] % 2:
            pointer += 1
            # 2.2. if the pointer is odd again, increment it by 1 again
            if arr[pointer] % 2:
                pointer += 1
                # 2.3. if the pointer is odd a 3rd time in a row, return True
                if arr[pointer] % 2:
                    return True
        # 2.4. increment the pointer by 1 each iteration of the while loop so that you skip all previously tested pointer values
        pointer += 1

    # 3. return False at the end if you never returned True
    return False


print(not threeConsecutiveOdds([2, 6, 4, 1]))
print(threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
