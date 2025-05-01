"""
LeetCode Problem: 408. Valid Word Abbreviation
Link: https://leetcode.com/problems/valid-word-abbreviation/
Difficulty: Easy
Topics: String, Two Pointers
"""


def validWordAbbreviation(word: str, abbr: str) -> bool:
    n_word = len(word)
    n_abbr = len(abbr)
    pointer_1 = 0
    pointer_2 = 0

    while pointer_2 < n_abbr:
        """
        pointer_1 = 0
        pointer_2 = 0
        end = 0
        num = 0
        """
        if abbr[pointer_2].isnumeric():
            if abbr[pointer_2] == "0":
                return False
            end = pointer_2
            while end < n_abbr and abbr[end].isnumeric():
                end += 1
            num = abbr[pointer_2: end]
            pointer_1 += int(num)
            pointer_2 = end
        else:
            if (pointer_1 < n_word and word[pointer_1]) != (pointer_2 < n_abbr and abbr[pointer_2]):
                return False
            pointer_1 += 1
            pointer_2 += 1

    return pointer_1 == n_word and pointer_2 == n_abbr


print(validWordAbbreviation(word="internationalization", abbr="i12iz4n"))
print(not validWordAbbreviation(word="apple", abbr="a2e"))
