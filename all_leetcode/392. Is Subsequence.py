"""
LeetCode Problem: 392. Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/
Difficulty: Easy
Topics: Two Pointers, String
"""


def isSubsequence(s: str, t: str) -> bool:
    # 0. base case if s is an empty string return True
    if len(s) == 0:
        return True

    # 1. set the start pointer as 0
    start = 0
    x
    # 2. going thru t using i as a pointer, check to see if the characters match, if they do, increase the start pointer
    for i in range(len(t)):
        if s[start] == t[i]:
            start += 1
            # 2.1. if the start pointer is ever the same as length s, return True
            if start == len(s):
                return True

    # 3. return False at the end
    return False


print(isSubsequence(s="abc", t="ahbgdc"))
print(not isSubsequence(s="axc", t="ahbgdc"))
