from typing import List
import heapq


def kthSmallestPrimeFraction(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    heap = []

    for left in range(n - 1):
        left_num = arr[left]
        for right in range(left + 1, n):
            right_num = arr[right]
            heapq.heappush(heap, (-left_num / right_num, (left_num, right_num)))
            if len(heap) > k:
                heapq.heappop(heap)

    return list(heapq.heappop(heap)[1])


print(kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3) == [2, 5])
