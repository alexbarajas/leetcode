"""
Inversion is a strictly decreasing subsequence of length 3. More formally, given an array, p, an inversion in the array is any time some p[i] > p[j] > p[k] and i < j < k. Given an array of length n, find the number of inversions.

Example)
n = 5, arr = [5, 3, 4, 2, 1]
Array inversions are [5, 3, 2], [5,3,1], [5,4,2], [5,4,1], [5,2,1], [3,2,1], [4,2,1]

n = 4, arr = [4,2,2,1]
The only inversion is [4,2,1] and we do not count the duplicate inversion.
"""

def maxInversions(arr):
    # Write your code here
    answer = []
    n = len(arr)

    def backtrack(combination, index):
        if len(combination) == 3:
            answer.append(list(combination))
            return
        for i in range(index, n):
            if combination[-1] > arr[i]:
                combination.append(arr[i])
                backtrack(combination, i + 1)
                combination.pop()

    for i in range(n - 2):
        backtrack([arr[i]], i)

    return len(answer)

arr = [5, 3, 4, 2, 1]
print(maxInversions(arr))

arr = [8, 6, 1, 4, 5, 5, 5]
print(maxInversions(arr))
