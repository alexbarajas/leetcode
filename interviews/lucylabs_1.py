"""
Q2 - Priority Sorting
=====================

Summary
-------
Given two lists of strings, one a list of input words, and the other a list
of important words (in order of priority), sort the list of input words in
case-sensitive alphabetical order while ensuring that the important words, if
they exist in the list of words, are at the front and in priority order.

Inputs
------
words - a list of input words (list of strings)
important - a list of (unique) important words in priority order

Returns
-------
A the list of words in alphabetical order with any important words at the front

Examples
--------
Inputs:
    words = ["alpha", "eagle", "charlie", "delta", "bravo"]
    important = ["hotel", "delta", "alpha"]

Return:
    ["delta", "alpha", "bravo", "charlie", "eagle"]


Inputs:
    words = ["eagle", "charlie", "bravo", "delta", "alpha"]
    important = ["bravo", "charlie"]

Return:
    ["bravo", "charlie", "alpha", "delta", "eagle"]

Note
----
Feel free to use built-in sorting functions
"""


def priority_sort(words: list, important: list) -> list:
    # 0. set up a blank answer array
    answer = []
    # 1. append each word into the answer array if they are seen in the important array and exist in the words array
    for word in important:
        # 1.1 use a hashset of the words array to make the program quicker
        if word in set(words):
            answer.append(word)
            # 1.2 remove each word in words if it's been used
            words.remove(word)

    # 2. implement the quicksort algorithm so you can sort the remaining words in the words array
    def quickSort(list):
        if not list:
            return []
        return (quickSort([word for word in list[1:] if word < list[0]]) + [list[0]] + quickSort(
            [word for word in list[1:] if word >= list[0]]))

    # 3. add the quicksorted words array to the answer
    answer += quickSort(words)
    # 4. return the answer array
    return answer


words = ["alpha", "eagle", "charlie", "delta", "bravo"]
important = ["hotel", "delta", "alpha"]

print(priority_sort(words, important))

words = ["eagle", "charlie", "bravo", "delta", "alpha"]
important = ["bravo", "charlie"]

print(priority_sort(words, important))
