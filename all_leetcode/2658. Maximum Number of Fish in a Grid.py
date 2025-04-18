from typing import List


def findMaxFish(grid: List[List[int]]) -> int:
    ROWS = len(grid)
    COLUMNS = len(grid[0])
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    answer = 0

    def dfs(x, y, total):
        grid[x][y] = 0
        for dx, dy in DIRECTIONS:
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < ROWS and 0 <= new_y < COLUMNS and grid[new_x][new_y] > 0:
                total += dfs(new_x, new_y, grid[new_x][new_y])
        return total

    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] > 0:
                answer = max(answer, dfs(row, column, grid[row][column]))

    return answer


print(findMaxFish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]) == 7)
print(findMaxFish([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]) == 1)
