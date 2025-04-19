"""
LeetCode Problem: 3. Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium
Topics: Hash Table, Sliding Window
"""


def lengthOfLongestSubstring(s: str) -> int:
    # 0. base case if len(s) is less than 2, just return the length
    length = len(s)
    if length < 2:
        return length

    # 1. set up a hashset, a left pointer, and an answer variable
    hashset = set()
    left = 0
    answer = 0

    # 2. go thru s using a right pointer
    for right in range(length):
        # 2.1 if s[right] is in the hashset, remove it, and add 1 to left
        while s[right] in hashset:
            hashset.remove(s[left])
            left += 1
        # 2.2 regardless, add s[right] to the hashset, and get a new answer value comparing the current answer value with the length of the hashset
        hashset.add(s[right])
        # answer = max(answer, len(hashset))  # either this line or the line below it work
        answer = max(answer, right - left + 1)

    # 3. return the answer
    return answer


print(lengthOfLongestSubstring("abcabcbb") == 3)
print(lengthOfLongestSubstring("bbbbb") == 1)
print(lengthOfLongestSubstring("pwwkew") == 3)
