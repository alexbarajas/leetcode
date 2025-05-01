"""
LeetCode Problem: 202. Happy Number
Link: https://leetcode.com/problems/happy-number/
Difficulty: Easy
Topics: Hash Table, Match
"""


def isHappy(n: int) -> bool:
    # 1. set up a visited hashset
    visited = set()

    # 2. a while loop is used as long as n isn't 1
    while n != 1:
        # 2.1. if n has been visited, return False, if not then add it to visited
        if n in visited:
            return False
        visited.add(n)

        # 2.2. one line version of the lines below
        n = sum(int(num) ** 2 for num in str(n))

        # # 2.2. set up a temp variable as 0, and add the squares of each number in n to it
        # temp = 0
        # for num in str(n):
        #     temp += int(num) ** 2
        #
        # # 2.3. set n as the temp variable
        # n = temp

    # 3. return True if the while loop ends because n is 1
    return True


print(isHappy(19))
print(not isHappy(2))
