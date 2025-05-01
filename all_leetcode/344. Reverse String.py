"""
LeetCode Problem: 344. Reverse String
Link: https://leetcode.com/problems/reverse-string/
Difficulty: Easy
Topics: Two Pointers, String
"""

from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


print(reverseString(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"])
