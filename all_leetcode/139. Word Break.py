from typing import List
import collections

"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


# # this won't work because you can't return True in backtracking since it's done recursively and then pop from current afterwards
# def wordBreak(s: str, wordDict: List[str]) -> bool:
#     n = len(s)
#
#     def backtracking(index, current):
#         if index == n:
#             print("hi")
#             return True
#         for word in wordDict:
#             new_index = index + len(word)
#             if new_index <= n and word == s[index: new_index]:
#                 current.append(word)
#                 backtracking(new_index, current)
#                 current.pop()
#
#     if backtracking(0, []):
#         return True
#     return False

def wordBreak(s: str, wordDict: List[str]) -> bool:
    # 1. turn the array into a set, set up a queue, and a hashset for the visited word
    n = len(s)
    word_set = set(wordDict)
    queue = collections.deque()
    visited = set()

    # 2. start the program by appending 0 to the queue
    queue.append(0)

    # 3. as long as the queue exists, look for possible matches
    while queue:
        # 3.1 first, popleft the value from the queue and set it as the starting integer from s, and if it's in the visited set, continue, if not, add it to visited
        start = queue.popleft()
        if start in visited:
            continue
        visited.add(start)
        # 3.2 if start is not in visited, then go thru the words in word_set searching for a match
        for word in word_set:
            end = start + len(word)
            if s[start: end] == word:
                # 3.3 if there is a match then append the end value into the queue, and if end == n, then that means you got a perfect match, so return True
                queue.append(end)
                if end == n:
                    return True

    # 4. return False if all else fails
    return False


print(wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(not wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
