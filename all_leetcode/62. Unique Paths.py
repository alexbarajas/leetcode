def uniquePaths(m: int, n: int) -> int:
    # 0. base case, if either number is 1, return 1
    if m == 1 or n == 1:
        return 1

    # 1. set up the dp matrix
    dp = [[1 for i in range(n)] for j in range(m)]

    # 2. go thru the matrix, since the robot can only go down or right, each space is the sum of the space to the left, and the space above it. start from the 1th index for each row and column because the spaces on the upper and left edges are all 1
    for row in range(1, m):
        for column in range(1, n):
            dp[row][column] = dp[row - 1][column] + dp[row][column - 1]

    # 3. return the space in the matrix in the bottom right corner
    return dp[-1][-1]


print(uniquePaths(m=3, n=7) == 28)
