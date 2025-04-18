"""
Write a function:

def solution(S)

that, given a string S, returns an integer that represents the number of ways in which
we can select a non-empty substring of S where all of the characters of the substring
are identical. Two substrings with the same letters but different locations are still
considered different.

For example, the string "zzzyz" contains 8 such substrings. Four instances of "z",
two of "zz", one of "zzz" and one instance of "y".

String "k" contains only one such substring: "k".

The length of S will be between 1 and 100, inclusive.

Each character in S will be a lowercase letter (a-z).
"""


def solution(S):
    score = 0
    for i in S:
        score += 1
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            score += 1
        if S[i] == S[i + 1] == S[i + 2]:
            score += 1
    return score

S = "zzzzzzzzzyzzyzy"

print(solution(S))









