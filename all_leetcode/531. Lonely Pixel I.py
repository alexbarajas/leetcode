"""
LeetCode Problem: 531. Lonely Pixel I
Link: https://leetcode.com/problems/lonely-pixel-i/
Difficulty: Medium
Topics: Array, Matrix, Hash Table
"""

from typing import List


def findLonelyPixel(picture: List[List[str]]) -> int:
    m = len(picture)
    n = len(picture[0])

    rows = [0 for i in range(m)]
    columns = [0 for j in range(n)]

    for row in range(m):
        for column in range(n):
            if picture[row][column] == "B":
                rows[row] += 1
                columns[column] += 1

    return sum(1 for row in range(m) for column in range(n) if
               picture[row][column] == "B" and rows[row] == 1 and columns[column] == 1)

    # answer = 0
    # for row in range(m):
    #     for column in range(n):
    #         if picture[row][column] == "B" and rows[row] == 1 and columns[column] == 1:
    #             answer += 1

    # return answer


print(findLonelyPixel([["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]) == 3)
print(not findLonelyPixel([["B", "B", "B"], ["B", "B", "W"], ["B", "B", "B"]]))
