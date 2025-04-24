"""
LeetCode Problem: 9. Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/
Difficulty: Easy
Topics: Math

Given an integer x, return true if x is a palindrome, and false otherwise.
"""


def isPalindrome(x: int) -> bool:
    if x < 0:  # takes care of all negative values
        return False

    divider = 1  # starts up the divider
    while x >= 10 * divider:
        divider *= 10  # makes the divider the same amount of values as x

    while x:  # while x is not 0
        # print(x, x // divider, x % 10)
        # x // divider gets the value at the front
        # x % 10 gets the value at the back
        if x // divider != x % 10:  # // == integer division, % == remainder of division
            return False
        # x % divider gets rid of the value at the front
        # x // 10 gets rid of the value at the back
        x = (x % divider) // 10  # shift to the next value
        divider //= 100  # take off the last 2 digits, you do 2 because you checked a value from both sides

    return True


print(isPalindrome(121))
print(not isPalindrome(-121))
print(not isPalindrome(10))
print(isPalindrome(1221))
