"""
a sentence is defined as a string of space-separated words that starts with a capital letter followed by lowercase letters and spaces, and ends with a period. rearrange the words in a sentence while respecting the folliwig conditions:
1. each word is ordered by length, ascending
2. words of equal length must appear in the same order as in the original sentence
"""


def arrange(sentence):
    words = sentence.split(" ")
    hashmap = {}

    for word in words:
        word_length = len(word)
        hashmap[word_length] = hashmap.get(word_length, []) + [word.lower()]

    result = ""
    for word_lengths in sorted(hashmap.keys()):
        for word in hashmap[word_lengths]:
            if not result:
                result = word.capitalize()
            else:
                result += " " + word

    return result + "."


print(arrange("Cats and hats") == "And cats hats.")
