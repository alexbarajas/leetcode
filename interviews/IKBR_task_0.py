"""
you are given a string consisting of lowercase letters of the english alphabet.
you must split this string into a minimal number of substrings
in such a way that no leter occurs more than once in each substring.
"""





def solution(S):
    if len(S) <= 1:
        return len(S)

    hashset = set()
    count = 1
    for letter in S:
        if letter in hashset:
            hashset = set()
            hashset.add(letter)
            count += 1
        else:
            hashset.add(letter)

    return count


S = "abacdec"
print(solution(S))

S = "cycle"
print(solution(S))

S = "world"
print(solution(S))

S = "abba"
print(solution(S))

S = "dddd"
print(solution(S))