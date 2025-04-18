def maximumLength(s: str) -> int:
    hashmap = {}
    current_length = 1

    def fill_hashmap(letter, length):
        length_of_string = length
        while length > 0:
            hashmap[letter * length] = hashmap.get(letter * length, 0) + length_of_string - length + 1
            length -= 1

    for i in range(1, len(s)):
        current = s[i]
        previous = s[i - 1]
        if current == previous:
            current_length += 1
        else:
            fill_hashmap(previous, current_length)
            current_length = 1

    fill_hashmap(s[-1], current_length)

    answer = -1
    for combo, count in hashmap.items():
        if count >= 3:
            answer = max(answer, len(combo))

    return answer


print(maximumLength(s="aaaa") == 2)
print(maximumLength(s="abcdef") == -1)
