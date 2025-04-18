
def canMakeSubsequence(str1: str, str2: str) -> bool:
    pointer1 = len(str1) - 1
    pointer2 = len(str2) - 1

    while pointer1 >= 0 and pointer2 >= 0:
        character1 = ord(str1[pointer1])
        character2 = ord(str2[pointer2])

        if character1 == character2 or character2 in [character1, character1 + 1, character1 - 25]:
            pointer2 -= 1

        pointer1 -= 1

    return pointer2 == -1

print(canMakeSubsequence(str1 = "abc", str2 = "ad"))
print(canMakeSubsequence(str1 = "zc", str2 = "ad"))
print(canMakeSubsequence(str1 = "z", str2 = "z"))
