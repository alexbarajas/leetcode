"""
Given an array with the lengths of various metal rods, repeatedly perform the following:
1. count the number of rods
2. find the rod(s) with the shortest length
3. discard any rod of that length
4. cut that shortest length from each of the longer rods. these are offcuts
5. discard all offcuts
6. repeat until there are no more rods

return an array with the number of rods at the start of each turn
"""

import heapq
def rodOffset(lengths):
    result = []

    heap = []
    for length in lengths:
        heapq.heappush(heap, length)

    current_length = len(lengths)

    while heap:
        result.append(current_length)
        cut_length = heapq.heappop(heap)
        new_heap = []
        current_length = 0
        for i in range(len(heap)):
            current_value = heapq.heappop(heap) - cut_length
            if current_value:
                heapq.heappush(new_heap, current_value)
                current_length += 1
        heap = new_heap

    return result


print(rodOffset([1, 1, 3, 4]) == [4, 2, 1])