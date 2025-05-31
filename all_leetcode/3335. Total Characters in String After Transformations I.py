"""
LeetCode Problem: 3335. Total Characters in String After Transformations I
Link: https://leetcode.com/problems/total-characters-in-string-after-transformations-i/
Difficulty: Medium
Topics: 1D Dynamic Programming, String
"""


def lengthAfterTransformations(s: str, t: int) -> int:
    MOD = 10 ** 9 + 7
    count = [0] * 26

    for letter in s:
        count[ord(letter) - ord("a")] += 1

    for _ in range(t):
        current = [0] * 26
        current[0] = count[25]  # count[25] is from "z" which turns to "ab"
        current[1] = (count[25] + count[
            0]) % MOD  # count[25] is from "z" which turns to "ab", count[0] is from "a" which turns to "b"
        for i in range(2, 26):
            current[i] = count[i - 1]
        count = current

    return sum(count) % MOD


print(lengthAfterTransformations(s="abcyy", t=2) == 7)
