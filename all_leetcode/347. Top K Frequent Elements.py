import heapq
import collections
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    # # SOLUTION 1: easy to follow
    # # 1. set up a hashmap with each num in nums and their count
    # hashmap = collections.Counter(nums)

    # # 2. set up a heap and push (-count, number) from the hashmap, do -count so it becomes easy to pop from the heap
    # heap = []
    # for number, count in hashmap.items():
    #     heapq.heappush(heap, (-count, number))

    # # 3. set up an empty array and append the keys belonging to the k smallest negative values
    # answer = []
    # while heap and k > 0:
    #     answer.append(heapq.heappop(heap)[1])
    #     k -= 1

    # # 4. return the answer array
    # return answer

    # SOLUTION 2: reverses the array at the end
    # 1. set up a hashmap with each num in nums and their count
    hashmap = collections.Counter(nums)

    # 2. set up a heap and push (-value, key) from the hashmap, do -value so it becomes easy to pop from the heap
    heap = []
    for num, count in hashmap.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)

    # 3. set up an empty array and append the keys belonging to the k smallest negative values
    answer = []
    for i in range(k):
        answer.append(heapq.heappop(heap)[1])

    # 4. return the answer array
    return answer[::-1]  # this uses reversed in case they as for it to be in the correct order


print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2])
