from typing import List


def maxChunksToSorted(arr: List[int]) -> int:
    n = len(arr)
    chunks = 0
    max_element = 0

    for i in range(n):
        # we keep track of the max_element because if we have a
        # max_element, then that means every element before it
        # is lower than the max_element, so once the max_element
        # is equal to i, it means a chunk could be had there
        max_element = max(max_element, arr[i])
        chunks += max_element == i

    return chunks


print(maxChunksToSorted([4, 3, 2, 1, 0]) == 1)
print(maxChunksToSorted([1, 0, 2, 3, 4]) == 4)
