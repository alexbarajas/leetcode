from typing import List


def maximumBeauty(nums: List[int], k: int) -> int:
    nums.sort()
    answer = 0

    left = 0
    for right in range(len(nums)):
        while nums[right] - nums[left] > 2 * k:
            left += 1
        answer = max(answer, right - left + 1)

    return answer


print(maximumBeauty(nums = [4,6,1,2], k = 2) == 3)
print(maximumBeauty(nums = [1,1,1,1], k = 10) == 4)
