from typing import List


def mostPoints(questions: List[List[int]]) -> int:
    # 1. get n and set up dp to have n + 1 values of 0. we do n + 1 because the last value in the array is in case the current question has a jump that's past the last question
    n = len(questions)
    dp = [0 for i in range(n + 1)]

    # 2. start from the back of questions, and fill in dp accordingly
    for i in range(n - 1, -1, -1):
        points, jump = questions[i]
        # 2.1. dp[i] is the max between the points for the current question, and the max points if you skip the question
        # solve = questions[i][0] + dp[min(n, i + jump + 1)]
        # skip = dp[i + 1] because the max points is always the next dp value
        dp[i] = max(points + dp[min(n, i + jump + 1)], dp[i + 1])

    # 3. return dp[0] since it'll have the max points you can get
    return dp[0]


print(mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]) == 5)
print(mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 7)
