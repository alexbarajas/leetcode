"""
LeetCode Problem: 2900. Longest Unequal Adjacent Groups Subsequence I
Link: https://leetcode.com/longest-unequal-adjacent-groups-subsequence-i/
Difficulty: Easy
Topics: 1D Dynamic Programming, Greedy
"""

from typing import List


def getLongestSubsequence(words: List[str], groups: List[int]) -> List[str]:
    # this uses O(n) time and O(n) space complexities. if you want to use O(n) time and O(1) space, go thru the arrays once, don't make arrays to keep track of the possible answers, then once you have whether the answer starts with an even or odd, make that array and return it. now you won't need any additional space in addition to the array you'll be returning
    evenStart = 0
    oddStart = 0
    even = False
    odd = False

    evenAnswer = []
    oddAnswer = []

    for i in range(len(groups)):
        current = groups[i]
        if current == 0:
            if not even:
                even = True
                evenStart += 1
                evenAnswer.append(words[i])
            if odd:
                odd = False
                oddStart += 1
                oddAnswer.append(words[i])
        if current == 1:
            if even:
                even = False
                evenStart += 1
                evenAnswer.append(words[i])
            if not odd:
                odd = True
                oddStart += 1
                oddAnswer.append(words[i])

    return evenAnswer if evenStart > oddStart else oddAnswer


print(getLongestSubsequence(words=["e", "a", "b"], groups=[0, 0, 1]) in [["e", "b"], ["a", "b"]])
