"""
return the first instance of the most seen character in a string

Example 1:
s = "leetcooode"
answer = "e"

"e" and "o" both occur 3 times in the string, but "e" is observed first
"""

def repeat(s):
    hashmap = {}
    for character in s:
        hashmap[character] = hashmap.get(character, 0) + 1

    maxCount = max(hashmap.values())

    for character in s:
        if hashmap[character] == maxCount:
            return character

s = "leetcooode"
print(repeat(s))