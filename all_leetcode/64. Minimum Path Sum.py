"""
LeetCode Problem: 64. Minimum Path Sum
Link: https://leetcode.com/problems/minimum-path-sum/
Difficulty: Medium
Topics: 2D Dynamic Programming, Matrix
"""

from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    # 1. go thru every space in the grid, if either i or j are 0, act accordingly, otherwise add the min of the spaces to the left and north of the current space
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0:
                grid[i][j] += grid[i - 1][j]
            else:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    # 2. return the space in the bottom right corner
    return grid[-1][-1]


print(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7)
