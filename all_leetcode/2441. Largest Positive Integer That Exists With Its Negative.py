from typing import List


def findMaxK(nums: List[int]) -> int:
    hashset = set()
    answer = -1

    for num in nums:
        if num * -1 in hashset:
            answer = max(answer, abs(num))
        else:
            hashset.add(num)

    return answer


print(findMaxK([-1, 2, -3, 3]) == 3)
print(findMaxK([-1, 10, 6, 7, -7, 1]) == 7)
print(findMaxK([-10, 8, 6, 7, -2, -3]) == -1)
