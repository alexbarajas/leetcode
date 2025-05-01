"""
LeetCode Problem: 387. First Unique Character in a String
Link: https://leetcode.com/problems/first-unique-character-in-a-string/
Difficulty: Easy
Topics: Hash Table, String
"""
import collections


def firstUniqChar(s: str) -> int:
    # 1. set up a hashmap and put each letter and its count from s into it
    hashmap = collections.Counter(s)

    # 2. now go thru the indices in s, and check if the corresponding letter for that index is in the hashmap, if it is and the count is 1, return the index
    for i in range(len(s)):
        # 2.1 remember that dicts in python 3.7 and later are ordered
        if hashmap[s[i]] == 1:
            return i

    # 3. else return -1
    return -1


print(firstUniqChar("leetcode") == 0)
print(firstUniqChar("loveleetcode") == 2)
