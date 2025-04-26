"""
LeetCode Problem: 49. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Topics: Hash Table, Array, String
"""

from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # SOLUTION 1: easy to understand
    # 1. set up a hashmap to match the anagrams
    hashmap = {}

    # 2. go thru each word in strs, and put it in the hashmap according to its sorted_word
    for word in strs:
        # 2.1. sort the word and see if it's in the hashmap
        anagram = "".join(sorted(word))  # remember to join the sorted word via an empty string
        # 2.2. if the sorted_word is not in the hashmap, add the word in an array, if it is, add the word to the existing array
        hashmap[anagram] = hashmap.get(anagram, []) + [word]

    # 3. return the values of the hashmap
    return list(hashmap.values())


def groupAnagrams1(strs: List[str]) -> List[List[str]]:
    # SOLUTION 2: more efficient, with character counts
    hashmap = {}

    for word in strs:
        count = [
                    0] * 26  # this saves time because you're not sorting the letters for each word, instead you are just incrementing the count for each letter as it's seen
        for character in word:
            count[ord(character) - ord("a")] += 1
        hashmap[tuple(count)] = hashmap.get(tuple(count), []) + [word]

    return list(hashmap.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
print(groupAnagrams([""]) == [[""]])
print(groupAnagrams(["a"]) == [["a"]])
print(groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
print(groupAnagrams1([""]) == [[""]])
print(groupAnagrams1(["a"]) == [["a"]])
