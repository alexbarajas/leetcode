"""
LeetCode Problem: 389. Find the Difference
Link: https://leetcode.com/problems/find-the-difference/
Difficulty: Easy
Topics: Hash Table, String, Bit Manipulation
"""


def findTheDifference(s: str, t: str) -> str:
    # # SOLUTION 1: using a hashmap
    # hashmap = collections.Counter(s)

    # for letter in t:
    #     if letter not in hashmap or hashmap[letter] == 0:
    #         return letter
    #     else:
    #         hashmap[letter] -= 1

    # SOLUTION 2: using bit manipulation
    answer = 0

    for letter in s:
        answer ^= ord(letter)
    for letter in t:
        answer ^= ord(letter)

    return chr(answer)


print(findTheDifference(s="abcd", t="abcde") == "e")
print(findTheDifference(s="", t="y") == "y")
