import collections


def charFreq(sentence):
    return collections.Counter(sentence)


print(charFreq("data") == {'a': 2, 'd': 1, 't': 1})
