from typing import List

"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    n = len(s)
    answer = []

    def backtracking(index, current):
        if index == n:
            answer.append(" ".join(current))
            return
        for word in wordDict:
            new_index = index + len(word)
            if new_index <= n and word == s[index: new_index]:
                current.append(word)
                backtracking(new_index, current)
                current.pop()

    backtracking(0, [])

    return answer


print(wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]) == ["cat sand dog", "cats and dog"])
print(wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]) == [])
print(wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"]) == [
    "pine apple pen apple", "pine applepen apple", "pineapple pen apple"])
