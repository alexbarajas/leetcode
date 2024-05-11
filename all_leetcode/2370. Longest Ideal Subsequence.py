def longestIdealString(s: str, k: int) -> int:
    n = len(s)
    dp = [0] * 26
    answer = 0

    for i in range(n):
        current = ord(s[i]) - ord("a")
        best = 0
        for previous in range(max(0, current - k), min(26, current + k + 1)):
            best = max(best, dp[previous])
        dp[current] = max(dp[current], best + 1)
        answer = max(answer, dp[current])

    return answer


print(longestIdealString(s="acfgbd", k=2) == 4)
print(longestIdealString(s="abcd", k=3) == 4)
print(longestIdealString(s="acfgbhiodaed", k=3) == 7)
print(longestIdealString(s="eduktdb", k=15) == 5)
print(longestIdealString(s="azaza", k=25) == 5)
