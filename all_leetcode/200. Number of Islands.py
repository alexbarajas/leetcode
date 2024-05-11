from typing import List
import collections


def numIslands(grid: List[List[str]]) -> int:
    # SOLUTION 1: BFS
    ROWS = len(grid)
    COLUMNS = len(grid[0])
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = collections.deque()
    answer = 0

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
    # ROWS = len(grid)
    # COLUMNS = len(grid[0])
    # DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # answer = 0
    #
    # def dfs(x, y):
    #     if grid[x][y] == "1":
    #         grid[x][y] = "0"
    #         for dx, dy in DIRECTIONS:
    #             new_x = x + dx
    #             new_y = y + dy
    #             if 0 <= new_x < ROWS and 0 <= new_y < COLUMNS and grid[new_x][new_y] == "1":
    #                 dfs(new_x, new_y)
    #
    # for row in range(ROWS):
    #     for column in range(COLUMNS):
    #         if grid[row][column] == "1":
    #             answer += 1
    #             dfs(row, column)
    #
    # return answer


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(numIslands(grid) == 1)

grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
print(numIslands(grid) == 3)
