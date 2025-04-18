import heapq
from typing import List


def minOperations(nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    moves = 0

    # once nums[0] >= k, that means every value in the array exceeds the threshold
    while nums[0] < k:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        heapq.heappush(nums, a * 2 + b)
        moves += 1

    return moves


print(minOperations(nums=[2, 11, 10, 1, 3], k=10) == 2)
print(minOperations(nums=[1, 1, 2, 4, 9], k=20) == 4)
