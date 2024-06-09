def wordPattern(pattern: str, s: str) -> bool:
    # 1. first split up s and make sure it's the same length as pattern
    s = s.split(" ")
    n = len(pattern)
    if n != len(s):
        return False

    # 2. set up a hashmap to store the values in pattern with the keys in s, and a hashset to store the seen characters in s
    hashmap = {}  # to check if characters in pattern have not been seen
    seen = set()  # to check if characters in s have not been seen

    # 3. go through pattern and s, matching then in the hashmap, and adding s to the hashset
    for i in range(n):
        # 3.1 pattern[i] has not been seen so add it to the hashmap, but if the s[i] corresponding to that pattern[i] has been seen, return False
        if pattern[i] not in hashmap:
            hashmap[pattern[i]] = s[i]
            if s[i] in seen:
                return False
        # 3.2 pattern[i] has been seen, so see if the keys match up with the current s[i], if not, return False
        elif pattern[i] in hashmap:
            if hashmap[pattern[i]] != s[i]:
                return False
        # 3.3 always add s[i] to seen regardless
        seen.add(s[i])

    # 4. if False was never returned, then return True
    return True


print(wordPattern(pattern="abba", s="dog cat cat dog"))
print(not wordPattern(pattern="abba", s="dog cat cat fish"))
