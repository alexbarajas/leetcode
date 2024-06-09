

def numberOfSubstrings(s: str) -> int:
    # SOLUTION 1: uses a hashmap for counts
    total = 0
    count = {}

    for character in s:
        count[character] = count.get(character, 0) + 1
        total += count[character]

    return total

    # # SOLUTION 2: uses an array for counts
    # total = 0
    # counts = [0] * 26
    # for letter in s:
    #     counts[ord(letter) - 97] += 1
    #     total += counts[ord(letter) - 97]
    # return total


print(numberOfSubstrings("abcba") == 7)
print(numberOfSubstrings("abacad") == 9)
