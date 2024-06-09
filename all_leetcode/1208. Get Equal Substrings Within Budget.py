def equalSubstring(s: str, t: str, maxCost: int) -> int:
    n = len(s)
    costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
    answer = 0

    left = 0
    prefixSum = 0
    for right in range(n):
        prefixSum += costs[right]
        while prefixSum > maxCost:
            prefixSum -= costs[left]
            left += 1
        answer = max(answer, right - left + 1)

    return answer


print(equalSubstring(s="abcd", t="bcdf", maxCost=3) == 3)
print(equalSubstring(s="abcd", t="cdef", maxCost=3) == 1)
print(equalSubstring(s="abcd", t="acde", maxCost=0) == 1)
