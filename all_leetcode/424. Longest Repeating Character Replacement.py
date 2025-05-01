"""
LeetCode Problem: 424. Longest Repeating Character Replacement
Link: https://leetcode.com/problems/longest-repeating-character-replacement/
Difficulty: Medium
Topics: Hash Table, Sliding Window, String
"""


def characterReplacement(s: str, k: int) -> int:
    # 1. set up n, an empty hashmap, and the answer variable
    n = len(s)
    hashmap = {}
    answer = 0

    # 2. set up the left pointer as 0 and make a for loop for the right pointer
    left = 0
    for right in range(n):
        # 2.1. update the hashmap with the current right letter
        hashmap[s[right]] = hashmap.get(s[right], 0) + 1
        # 2.2. once the size of the current window is greater than the size of the most common character + k, remove the left letter from the window and increment left until it isn't
        while right - left + 1 > max(hashmap.values()) + k:
            hashmap[s[left]] -= 1
            left += 1
        # 2.3. update the window at the end of each iteration of the for loop
        answer = max(answer, right - left + 1)

    # 3. at the end, return the answer
    return answer


print(characterReplacement(s="ABAB", k=2) == 4)
print(characterReplacement(s="AABABBA", k=1) == 4)
