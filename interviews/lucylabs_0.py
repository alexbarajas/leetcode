"""
Q1 - Split Names
================

Summary
-------
Write a function to split a delimited input string into component parts and
return the parts as a dict where the keys are the supplied names.

* The names of the parts (i.e. keys of the returned dict) are supplied as an
  input list in the order they appear in the input string.

* If a named part is missing, return None for that part.

* Extra parts in the src string should be ignored.

Inputs
------
src   -- a string with parts seperated by a delimiter
delim -- a delimiter that seperates component parts of src
names -- a list of names of the component parts, in order

Returns
-------
A dict with the part names as the keys and values from the corresponding input
src string part positions

Examples
--------
Inputs:
    src   = "1234::Alpha::Bravo::Charlie"
    delim = "::"
    names = ['foo', 'bar', 'baz']

Return:
    {'foo': '1234', 'bar': 'Apha', 'baz': 'Bravo'}


Inputs:
    src   = "Alpha//Charlie"
    delim = "/"
    names = ['a', 'b', 'c']

Return:
    {'a': 'Alpha', 'b': '', 'c': 'Charlie'}


Inputs:
    src   = "foo.bar"
    delim = "."
    names = ['a', 'b', 'c', 'd']

Return:
    {'a': 'foo', 'b': 'bar', 'c': None, 'd': None}
"""


def split_names(src: str, delim: str, names: list) -> dict:
    # 0. first we set up the src by splitting it according to the delim, and by making a setup hashmap
    # for the split src values, and an answer hashmap where everything is put together
    srcSplit = src.split(delim)
    setup = {}
    answer = {}
    # 1. go through every value in the split src list, and map it with its index in the setup hashmap
    for i in range(len(srcSplit)):
        setup[i] = srcSplit[i]
    # 2. map each src split value with each value in the names array if they have the same index
    for i in range(len(names)):
        if i in setup:
            answer[names[i]] = setup[i]
        # 2.1 if the names array is longer than the split src list, assign None to the names value in the answer array
        else:
            answer[names[i]] = None
    # 3. return the answer array
    return answer


src = "1234::Alpha::Bravo::Charlie"
delim = "::"
names = ['foo', 'bar', 'baz']

print(split_names(src, delim, names))

src = "Alpha//Charlie"
delim = "/"
names = ['a', 'b', 'c']

print(split_names(src, delim, names))

src = "foo.bar"
delim = "."
names = ['a', 'b', 'c', 'd']

print(split_names(src, delim, names))
