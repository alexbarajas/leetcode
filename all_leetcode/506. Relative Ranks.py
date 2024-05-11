import heapq
from typing import List


def findRelativeRanks(score: List[int]) -> List[str]:
    # 1. set up a heap
    heap = []

    # 2. for each score, push the negative score into the heap
    for i in score:
        heapq.heappush(heap, -i)

    # 3. set up a hashmap and pop the negative (reverting the value back to positive) score and give it a medal if it's one of the first 3 popped values
    hashmap = {}
    for i in range(len(heap)):
        if i == 0:
            hashmap[-heapq.heappop(heap)] = "Gold Medal"
        elif i == 1:
            hashmap[-heapq.heappop(heap)] = "Silver Medal"
        elif i == 2:
            hashmap[-heapq.heappop(heap)] = "Bronze Medal"
        else:
            hashmap[-heapq.heappop(heap)] = str(i + 1)

    # 4. make an array with the hashmap values that correspond with each score in the original score array
    return [hashmap[i] for i in score]


print(findRelativeRanks([5, 4, 3, 2, 1]) == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"])
