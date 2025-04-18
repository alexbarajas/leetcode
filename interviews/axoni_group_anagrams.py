"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""


def groupAnagrams(strs):
    # 1. set up a hashmap to match the anagrams, and an answer array that will be returned at the end
    hashmap = {}
    answer = []

    # 2. go thru each word in strs, and sort it, if that sorted word is not in the hashmap, add it and set it as [word], if it is in the hashmap, add that [word] to that key
    for word in strs:
        string = "".join(sorted(word))  # remember to join the sorted word via an empty string
        if string not in hashmap:
            hashmap[string] = [word]
        else:  # either of these 2 work
            # hashmap[string] += [word]
            hashmap[string].append(word)

    # 3. go thru the hashmap, adding each set of anagrams to the answer array
    for key, value in hashmap.items():
        answer.append(value)

    # 4. return the answer array
    return answer


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
