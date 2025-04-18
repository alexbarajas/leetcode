"""
Maximal Square
"""


def largestArea(samples):
    if not samples:  # check if a matrix exists
        return 0
    x = len(samples)  # gets number of rows
    y = len(samples[0])  # gets number of columns
    maximum = 0  # declares a maximum variable
    test = [[0] * (y + 1) for _ in range(x + 1)]  # expands the matrix by 1 column and row and uses it for tests
    for i in range(1, x + 1):  # these for loops check each value in the matrix
        for j in range(1, y + 1):
            if samples[i - 1][j - 1] == 1:  # this checks the value with the test matrix diagonally
                test[i][j] = 1 + min(test[i - 1][j], test[i][j - 1], test[i - 1][j - 1])  # gets the max size of a square
                maximum = max(maximum, test[i][j])  # sets a maximum length of a square
    return maximum ** 2  # returns the maximum length squared to give the area


samples = [[1,1,1,1,1], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,1,1]]
print(largestArea(samples))