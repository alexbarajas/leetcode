from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # # SOLUTION 1: easy to understand
    # hashmap = {}
    # for word in strs:
    #     anagram = "".join(sorted(word))
    #     hashmap[anagram] = hashmap.get(anagram, []) + [word]
    #
    # return list(hashmap.values())

    # SOLUTION 2: more efficient, with character counts
    hashmap = {}

    for word in strs:
        count = [0] * 26  # this saves time because you're not sorting the letters for each word, instead you are just incrementing the count for each letter as it's seen
        for character in word:
            count[ord(character) - ord("a")] += 1
        hashmap[tuple(count)] = hashmap.get(tuple(count), []) + [word]

    return list(hashmap.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
print(groupAnagrams([""]) == [[""]])
print(groupAnagrams(["a"]) == [["a"]])
