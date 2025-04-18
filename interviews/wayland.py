"""
how many runs can you make in lexicographical order
"""


# def howManyRuns(s):
#     if len(s) < 2:
#         return len(s)
#     hashmap = {}
#     for i in range(len(s)):
#         if i == 0:
#             hashmap[s[i]] = 1
#         else:
#             if s[i] in hashmap:
#                 hashmap[s[i]] += hashmap[s[i - 1]]
#             else:
#                 hashmap[s[i]] = 1
#     return hashmap[s[-1]]


def howManyRuns(s):
    # find the unique characters in order
    chars = []
    for letter in s:
        if letter not in chars:
            chars.append(letter)

    # find indexes at which each char appears
    indexs = {a: [] for a in chars}
    for ind, letter in enumerate(s):
        indexs[letter].append(ind)

    for ind, letter in enumerate(chars):
        chars[ind] = indexs[letter]

    # we now have an 2D array that stores the indexes of each character, sorted in the order in which the
    # character appears in s e.g for s = "abcabc", chars = [[0, 3], [1, 4], [2, 5]] where chars[0] is the 'a'
    # indexes, chars[1] is the 'b' indexes and so on.

    def numberOfIncreasingPaths(chars, paths=None):

        if paths is None:
            paths = []
        if not chars:
            return len(paths)

        if not paths:
            paths = [[a] for a in chars[0]]
            return numberOfIncreasingPaths(chars[1:], paths)
        else:
            updated_paths = []
            for path in paths:
                root = path[-1]
                for elem in chars[0]:
                    curr_path = path.copy()
                    if elem > root:
                        curr_path.append(elem)
                        updated_paths.append(curr_path)
            paths = updated_paths
            return numberOfIncreasingPaths(chars[1:], paths)

    return numberOfIncreasingPaths(chars)


s = "abcc"  # supposed to be 2
print(howManyRuns(s))

s = "abcabc"  # supposed to be 4
print(howManyRuns(s))

s = "abcabcabc"  # supposed to be 10
print(howManyRuns(s))

s = "abcabcac"  # supposed to be 7
print(howManyRuns(s))


"""
abcc
123_
12_3
1112
"""

"""
abccc
123__
12_3_
11__3
11123
"""


"""
abcabc
123___
12___3
1___23
___123
111234
"""


"""
abcabcabc
123______
12___3___
12______3
1___23___
1___2___3
1______23
___123___
___12___3
___1___23
______123
1112346913
"""
