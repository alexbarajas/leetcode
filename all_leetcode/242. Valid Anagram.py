def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    character_hashmap = {}
    for i in range(len(s)):
        character_hashmap[s[i]] = character_hashmap.get(s[i], 0) + 1
        character_hashmap[t[i]] = character_hashmap.get(t[i], 0) - 1

    for letter, count in character_hashmap.items():
        if count != 0:
            return False

    return True


print(isAnagram(s="anagram", t="nagaram"))
print(not isAnagram(s="rat", t="car"))
