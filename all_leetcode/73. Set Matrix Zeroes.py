"""
LeetCode Problem: 73. Set Matrix Zeroes
Link: https://leetcode.com/problems/set-matrix-zeroes/
Difficulty: Medium
Topics: Array, Matrix
"""

from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])

    def makeStar(r, c):
        matrix[r][c] = "*"
        for i in range(m):
            if matrix[i][c] != 0:
                matrix[i][c] = "*"
        for j in range(n):
            if matrix[r][j] != 0:
                matrix[r][j] = "*"

    for row in range(m):
        for column in range(n):
            if matrix[row][column] == 0:
                makeStar(row, column)

    for row in range(m):
        for column in range(n):
            if matrix[row][column] == "*":
                matrix[row][column] = 0

    return matrix


print(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
print(setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]) == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
