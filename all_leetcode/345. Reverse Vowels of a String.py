"""
LeetCode Problem: 345. Reverse Vowels of a String
Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
Difficulty: Easy
Topics: Two Pointers, String
"""


def reverseVowels(s: str) -> str:
    # 1. set up a vowels hashmap and set up s to be an array of letters instead of a string
    vowels = {"a", "e", "i", "o", "u"}
    s = [letter for letter in s]

    # 2. set up the left and right pointers and start the while loop
    left = 0
    right = len(s) - 1
    while left < right:
        # 2.1. while the left letter is not a vowel, increment left
        while s[left].lower() not in vowels and left < right:
            left += 1
        # 2.2. while the right letter is not a vowel, increment right
        while s[right].lower() not in vowels and right > left:
            right -= 1
        # 2.3. once the left and right letters are both vowels, switch them, and then increment both pointers
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    # 3. at the end, return an empty string joined by the s array
    return "".join(s)


print(reverseVowels("IceCreAm") == "AceCreIm")
