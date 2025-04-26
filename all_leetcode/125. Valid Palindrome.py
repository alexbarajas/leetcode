"""
LeetCode Problem: 125. Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Topics: Two Pointers, String
"""


def isPalindrome(s: str) -> bool:
    # 1. come up with the left and right pointers first
    left = 0
    right = len(s) - 1

    # 2. while left < right, go thru the string
    while left < right:
        # 2.1. change the pointers at the start if their values are not alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        # 2.2. if the values do not match up, return False
        if s[left].lower() != s[right].lower():
            return False

        # 2.3. shift the pointers
        left += 1
        right -= 1

    # 3. return True at the end
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(not isPalindrome("race a car"))
print(isPalindrome(" "))
