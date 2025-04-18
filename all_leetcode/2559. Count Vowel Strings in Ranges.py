from typing import List


def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
    vowels = {"a", "e", "i", "o", "u"}

    prefixSum = 0
    for i in range(len(words)):
        if words[i][0] in vowels and words[i][-1] in vowels:
            prefixSum += 1
        words[i] = prefixSum

    answer = []
    for a, b in queries:
        # the reason we do - words[a - 1] if a != 0 is because,
        # let's say a = 2 and b = 2, if we do words[b] - words[a] we get 0,
        # but if we do words[b] - words[b - 1] we get the value of words[b],
        # because it'll subtract the value that came before it, so we'll
        # only take into account whether or not words[b] is a valid vowel string,
        # thus we'll return 1 if it's a vowel string or 0 otherwise
        answer.append(words[b] - (words[a - 1] if a != 0 else 0))

    return answer


print(vowelStrings(words=["aba", "bcb", "ece", "aa", "e"], queries=[[0, 2], [1, 4], [1, 1]]) == [2, 3, 0])
