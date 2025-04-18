from typing import List


def regionsBySlashes(grid: List[str]) -> int:
    n = len(grid)
    pixel_grid = [[0 for j in range(3 * n)] for i in range(3 * n)]
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    answer = 0

    def change(x, y, symbol):
        if symbol == "\\":
            start_x = x * 3
            start_y = y * 3
            for i in range(3):
                pixel_grid[start_x + i][start_y + i] = 1
        elif symbol == "/":
            start_x = (x + 1) * 3 - 1
            start_y = y * 3
            for i in range(3):
                pixel_grid[start_x - i][start_y + i] = 1
        elif symbol == 0:
            pixel_grid[x][y] = 1
            for dx, dy in DIRECTIONS:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < 3 * n and 0 <= new_y < 3 * n and pixel_grid[new_x][new_y] == 0:
                    change(new_x, new_y, 0)

    for x in range(n):
        for y in range(n):
            space = grid[x][y]
            if space == "/":
                change(x, y, "/")
            elif space == "\\":
                change(x, y, "\\")

    for x in range(3 * n):
        for y in range(3 * n):
            if pixel_grid[x][y] == 0:
                answer += 1
                change(x, y, 0)

    return answer


print(regionsBySlashes([" /", "/ "]) == 2)
print(regionsBySlashes(["/\\", "\\/"]) == 5)
