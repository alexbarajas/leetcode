"""
1. matrix summation


"""


def findBeforeMatrix(after):
    # 0. n will be at least 1, so thus so will m, so an array will always exist,
    # so a base case in case an array doesn't exist is not needed
    # 1. set up the variables for the length of the columns and rows
    COLUMNS = len(after)
    ROWS = len(after[0])
    # 2. make a copy of the after array and set it as the before array
    before = [[after[i][j] for j in range(ROWS)] for i in range(COLUMNS)]
    # 3. traverse the after array and move from the bottom right corner to either the top or the left,
    # and then do the other way, reducing before[i][j] by every value that came before it
    # in the range that you are traversing
    for i in range(COLUMNS - 1, -1, -1):  # moves from right to left
        for j in range(ROWS - 1, 0, -1):
            before[i][j] -= before[i][j - 1]
    for i in range(COLUMNS - 1, 0, -1):  # moves from down to up
        for j in range(ROWS - 1, -1, -1):
            before[i][j] -= before[i - 1][j]
    # 4. return the before array
    return before


after = [[1, 2], [3, 4]]
print(findBeforeMatrix(after))
