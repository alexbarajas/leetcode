"""
LeetCode Problem: 200. Number of Islands
Link: https://leetcode.com/problems/number-of-islands/
Difficulty: Medium
Topics: Array, Matrix, DFS. BFS
"""

import collections
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    # SOLUTION 1: BFS
    # 1. set up an answer variable, as well as ROWS, COLUMNS AND DIRECTIONS constants, and a queue
    answer = 0
    ROWS = len(grid)
    COLUMNS = len(grid[0])
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = collections.deque()

    def bfs(x, y):
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            if grid[x][y] == "1":  # this line helps against redundancy
                grid[x][y] = "0"
                for dx, dy in DIRECTIONS:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < ROWS and 0 <= new_y < COLUMNS and grid[new_x][new_y] == "1":
                        queue.append((new_x, new_y))

    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] == "1":
                answer += 1
                bfs(row, column)

    return answer

    # # SOLUTION 2: DFS
    # # 1. set up an answer variable, as well as ROWS, COLUMNS AND DIRECTIONS constants
    # answer = 0
    # ROWS = len(grid)
    # COLUMNS = len(grid[0])
    # DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    #
    # # 2. set up a backtrack function
    # def dfs(x, y):
    #     # 2.1. the backtrack function first sets the space on the grid to "0"
    #     if grid[x][y] == "1":
    #         grid[x][y] = "0"
    #         # 2.2. then for each direction in DIRECTIONS, make a new_x, and a new_y, and check if the coordinates are in the grid and the space is equal to "1", if it is start backtracking from that space
    #         for dx, dy in DIRECTIONS:
    #             new_x = x + dx
    #             new_y = y + dy
    #             if 0 <= new_x < ROWS and 0 <= new_y < COLUMNS and grid[new_x][new_y] == "1":
    #                 dfs(new_x, new_y)
    #
    # # 3. for each space in the grid, check if the space is == "1", and if it is increase the answer by 1, and start backtracking using that space
    # for row in range(ROWS):
    #     for column in range(COLUMNS):
    #         if grid[row][column] == "1":
    #             answer += 1
    #             dfs(row, column)
    #
    # # 4. return the answer
    # return answer


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(numIslands(grid) == 1)

grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
print(numIslands(grid) == 3)
