from typing import List


def findRepeatedDnaSequences(s: str) -> List[str]:
    n = len(s)
    answer = set()
    if n < 10:
        return list(answer)

    hashset = set()

    for i in range(n - 9):
        sequence = s[i: i + 10]
        if sequence in hashset:
            answer.add(sequence)
        else:
            hashset.add(sequence)

    return list(answer)


print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") in (
    ["AAAAACCCCC", "CCCCCAAAAA"], ['CCCCCAAAAA', 'AAAAACCCCC']))
