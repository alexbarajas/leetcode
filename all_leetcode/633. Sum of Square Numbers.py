"""
LeetCode Problem: 633. Sum of Square Numbers
Link: https://leetcode.com/problems/sum-of-square-numbers/
Difficulty: Medium
Topics: Math, Two Pointers, Binary Search
"""


def judgeSquareSum(c: int) -> bool:
    # # SOLUTION 1: 2 pointers
    # # 1. set up values for a and b at the ends of the possible values
    # a = 0
    # b = int(c ** 0.5)
    #
    # # 2. while a <= b, come up with a total of the sum of their squares
    # while a <= b:
    #     total = a ** 2 + b ** 2
    #     # 2.1. if the total is == c, return True
    #     if total == c:
    #         return True
    #     # 2.2. if the total is less than c, move a
    #     elif total < c:
    #         a += 1
    #     # 2.3. otherwise, move b
    #     else:
    #         b -= 1
    #
    # # 3. return False at the end
    # return False

    # SOLUTION 2: binary search
    for i in range(int(c ** 0.5) + 1):
        left = 0
        right = c
        while left <= right:
            midpoint = (right - left) // 2 + left
            current = i ** 2 + midpoint ** 2
            if current == c:
                return True
            if current > c:
                right = midpoint - 1
            else:
                left = midpoint + 1

    return False


print(judgeSquareSum(5))
print(not judgeSquareSum(3))
