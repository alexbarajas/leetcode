"""
LeetCode Problem: 242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Topics: Hash Table, String
"""


def isAnagram(s: str, t: str) -> bool:
    # # SOLUTION 1: hashmaps
    # # 0. base case, if the lengths of s and t are different, return False
    # if len(s) != len(t):
    #     return False

    # # 1. set up a hashmap with the counts of the letters in s
    # s_hashmap = collections.Counter(s)

    # # 2. compare the letters in t to the s_hashmap, if they don't match up return False
    # for letter in t:
    #     if letter not in s_hashmap or s_hashmap[letter] == 0:
    #         return False
    #     # 2.1. if False wasn't returned, reduce the count of that letter by 1
    #     s_hashmap[letter] -= 1

    # # 3. return True if the strings match up
    # return True

    # # SOLUTION 2: collections.Counter
    # if len(s) != len(t):
    #     return False

    # return collections.Counter(s) == collections.Counter(t)

    # SOLUTION 3: 1 hashmap, best for unicode problem
    if len(s) != len(t):
        return False

    character_hashmap = {}
    for i in range(len(s)):
        character_hashmap[s[i]] = character_hashmap.get(s[i], 0) + 1
        character_hashmap[t[i]] = character_hashmap.get(t[i], 0) - 1

    for count in character_hashmap.values():
        if count != 0:
            return False

    return True


print(isAnagram(s="anagram", t="nagaram"))
print(not isAnagram(s="rat", t="car"))
