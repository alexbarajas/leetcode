"""
Write a function:

def solution(S)

that, given a string S encoding a decimal integer N, returns a string representing the
Hexspeak representation H of N if H is a valid Hexspeak word, otherwise it should return "ERROR".

A decimal number can be converted to Hexspeak by first converting it to hexadecmal,
then converting the number 0 to the letter "O" and the number 1 to the letter "I".
A string is considered a valid Hexspeak  word if it consists of only the ABCDEFIO letters.

The input string S will represent a decimal integer between 1 and 1,000,000,000,000 inclusive.

Example:

If the input string S is "257", the decimal number it encodes is 257 which is written as
101 in hexadecimal. Since 1 and 0 represent "I" and "O", respectively, we should return "IOI"

If the input string is "3", it is written as 3 in hexadecimal, which does not represent a
Hexspeak letter, so we return "ERROR".

All answers should be in uppercase letters.
"""


def solution(X):
    # print(hex(int(X)))
    hexspeak_word = list(hex(int(X)).lstrip("0x").rstrip("L"))
    # print(hexspeak_word)
    for index in range(0, len(hexspeak_word)):
        letter = hexspeak_word[index]
        if letter == "1":
            hexspeak_word[index] = "I"
        elif letter == "0":
            hexspeak_word[index] = "O"
        elif letter.isdigit():
            return "ERROR"

    return "".join(hexspeak_word)


print(solution("257"))








