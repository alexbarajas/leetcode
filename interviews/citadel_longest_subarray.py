def maxLength(a, k):
    left = 0
    right = 0
    n = len(a)
    currentLength = 0
    currentSum = 0

    while right < n:
        currentSum += a[right]
        if currentSum <= k:
            currentLength = max(currentLength, right - left + 1)
            right += 1
        else:
            currentSum -= a[left]
            left += 1
            right += 1

    return currentLength


a = [1, 2, 3]
k = 4
print(maxLength(a, k))

a = [3, 1, 2, 1]
k = 4
print(maxLength(a, k))
