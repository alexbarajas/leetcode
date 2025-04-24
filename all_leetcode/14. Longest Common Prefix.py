"""
LeetCode Problem: 14. Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/
Difficulty: Easy
Topics: String

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    answer = ""
    if len(strs) == 1:
        return strs[0]

    for i in range(min(len(word) for word in strs)):
        start = strs[0][i]
        # you can start checking from strs[1] because the longest common prefix would have to have strs[0][i] for it to have a length of i
        for word in strs[1:]:
            if word[i] != start:
                return word[:i]
        answer += start

    return answer


print(longestCommonPrefix(["flower", "flow", "flight"]) == "fl")
print(longestCommonPrefix(["ab", "a"]) == "a")
print(longestCommonPrefix(["", ""]) == "")
