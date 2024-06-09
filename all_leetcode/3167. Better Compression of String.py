
def betterCompression(compressed: str) -> str:
    hashmap = {}
    n = len(compressed)
    i = 0

    while i < n:
        letter = compressed[i]
        end = i + 1
        while end < n and compressed[end].isnumeric():
            end += 1
        count = int(compressed[i + 1: end])
        i = end
        hashmap[letter] = hashmap.get(letter, 0) + int(count)

    answer = ""

    for letter in sorted(hashmap.keys()):
        answer += letter + str(hashmap[letter])

    return answer


print(betterCompression("a3c9b2c1") == "a3b2c10")
print(betterCompression("i10g6u6") == "g6i10u6")
