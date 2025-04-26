"""
LeetCode Problem: 131. Palindrome Partitioning
Link: https://leetcode.com/problems/palindrome-partitioning/
Difficulty: Medium
Topics: String, 1D Dynamic Programming
"""

from typing import List


def partition(s: str) -> List[List[str]]:
    # SOLUTION 1: doesn't use a global array for the combinations
    answer = []
    n = len(s)

    def isPalindrome(string, left, right):
        while left <= right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True

    def dfs(start, current):
        if start == n:
            answer.append(list(current))
            return
        for i in range(start, n):
            if isPalindrome(s, start, i):
                current.append(s[start: i + 1])
                dfs(i + 1, current)
                current.pop()

    dfs(0, [])

    return answer

    # # SOLUTION 2: uses a global array for the combinations
    # answer = []
    # combination = []
    # n = len(s)
    #
    # def isPalindrome(string, left, right):
    #     while left <= right:
    #         if string[left] == string[right]:
    #             left += 1
    #             right -= 1
    #         else:
    #             return False
    #     return True
    #
    # def dfs(start):
    #     if start == n:
    #         answer.append(combination[:])
    #         return
    #     for i in range(start, n):
    #         if isPalindrome(s, start, i):
    #             combination.append(s[start: i + 1])
    #             dfs(i + 1)
    #             combination.pop()
    #
    # dfs(0)
    #
    # return answer


print(partition("aab") == [["a", "a", "b"], ["aa", "b"]])
print(partition("a") == [["a"]])
print(partition("aa") == [["a", "a"], ["aa"]])
