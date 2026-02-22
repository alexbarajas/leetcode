"""
LeetCode Problem: 386. Lexicographical Numbers
Link: https://leetcode.com/problems/lexicographical-numbers/
Difficulty: Medium
Topics: DFS
Description: Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space.
"""

from typing import List


def lexicalOrder(n: int) -> List[int]:
    # 1. set up the answer array and set the current variable as 1
    answer = []
    current = 1

    # 2. for i in range n...
    for i in range(n):
        # 2.1. first append current to the answer array
        answer.append(current)
        # 2.2. try to go deeper first, so if you can go to current * 10, go there
        if current * 10 <= n:
            current *= 10
        # 2.3. if you can't go deeper...
        else:
            # 2.3.1. fist check if the current number is n, if it is then floor divide it by 10 and add 1
            if current == n:
                current //= 10
            current += 1
            # 2.3.1. while current is divisible by 1, floor divide it by 10
            while current % 10 == 0:
                current //= 10

    # 3. return the answer at the end
    return answer


print(lexicalOrder(13) == [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9])
