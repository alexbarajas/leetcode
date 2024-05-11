from typing import List
import collections


def islandPerimeter(grid: List[List[int]]) -> int:
    # # SOLUTION 1: DFS
    # answer = 0
    # ROWS = len(grid)
    # COLUMNS = len(grid[0])
    # DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    #
    # def perimeter(x, y):
    #     total = 0
    #     for dx, dy in DIRECTIONS:
    #         new_x = x + dx
    #         new_y = y + dy
    #         if 0 <= new_x < ROWS and 0 <= new_y < COLUMNS and grid[new_x][new_y] == 1:
    #             continue
    #         else:
    #             total += 1
    #     return total
    #
    # for row in range(ROWS):
    #     for column in range(COLUMNS):
    #         if grid[row][column] == 1:
    #             answer += perimeter(row, column)
    #
    # return answer

    # SOLUTION 2: BFS
    ROWS = len(grid)
    COLUMNS = len(grid[0])
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = collections.deque()
    answer = 0

    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] == 1:
                queue.append((row, column))

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x == ROWS or new_y < 0 or new_y == COLUMNS or grid[new_x][new_y] == 0:
                answer += 1

    return answer


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(islandPerimeter(grid) == 16)
