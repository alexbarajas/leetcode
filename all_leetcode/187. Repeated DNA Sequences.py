"""
LeetCode Problem: 187. Repeated DNA Sequences
Link: https://leetcode.com/problems/repeated-dna-sequences/
Difficulty: Medium
Topics: Hash Table, String
"""

from typing import List


def findRepeatedDnaSequences(s: str) -> List[str]:
    # 0. if s is not big enough return an empty list
    n = len(s)
    if n < 10:
        return []

    # 1. set up hashsets for the seen strings, and for the answer
    hashset = set()
    answer = set()

    # 2. go thru s checking every sequence, if it's not in the hashset, add it, it if is in the hashset, add it to the answer
    for i in range(n - 9):
        sequence = s[i: i + 10]
        if sequence in hashset:
            answer.add(sequence)
        else:
            hashset.add(sequence)

    # 3. return the answer
    return list(answer)


print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") in (
    ["AAAAACCCCC", "CCCCCAAAAA"], ['CCCCCAAAAA', 'AAAAACCCCC']))
