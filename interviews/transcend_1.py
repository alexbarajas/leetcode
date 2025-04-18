
def longestIncreasingSubsequence(sequence):
    n = len(sequence)
    answer = 0
    longest_subsequence = []
    left = 0
    while left < n:
        right = left + 1
        while right < n and sequence[right - 1] < sequence[right]:
            right += 1
        if right - left > answer:
            answer = right - left
            longest_subsequence = sequence[left: right]
        left = right
    return longest_subsequence if answer >= 2 else []


print(longestIncreasingSubsequence([3, 0, 2, 2, 5, -43, -1, 0, 11, 9, 10]) == [-43, -1, 0, 11])
print(longestIncreasingSubsequence([1]) == [])
print(longestIncreasingSubsequence([3, 4, 1, 2]) == [3, 4])
print(longestIncreasingSubsequence([]) == [])
