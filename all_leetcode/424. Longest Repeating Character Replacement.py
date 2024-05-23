def characterReplacement(s: str, k: int) -> int:
    n = len(s)
    hashmap = {}
    answer = 0

    left = 0
    for right in range(n):
        hashmap[s[right]] = hashmap.get(s[right], 0) + 1
        while right - left + 1 > max(hashmap.values()) + k:
            hashmap[s[left]] -= 1
            left += 1
        answer = max(answer, right - left + 1)

    return answer


print(characterReplacement(s="ABAB", k=2) == 4)
print(characterReplacement(s="AABABBA", k=1) == 4)
