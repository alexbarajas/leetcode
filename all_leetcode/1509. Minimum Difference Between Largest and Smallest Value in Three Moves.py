import heapq
from typing import List


def minDifference(nums: List[int]) -> int:
    n = len(nums)

    if n <= 4:
        return 0

    # get the 4 largest and the 4 smallest elements and make them different sorted arrays
    four_smallest = sorted(heapq.nsmallest(4, nums))
    four_largest = sorted(heapq.nlargest(4, nums))

    answer = float("inf")

    for i in range(4):
        # let's say nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],
        # four_largest = [6, 7, 8, 9]
        # four_smallest = [1, 2, 3, 4]
        # we will compare, 6 and 1, 7 and 2, and so on
        # the reason we do this is that if we get rid of the 3 largest values, then we will end up comparing 1 from the front and 6 from the back,
        # but if we get rid of 1 number in front and 2 in the back, then we will end up comparing 2 from the front and 7 from the back,
        # the same goes for 8 and 3 and for 9 and 4, this is because those numbers are all the combinations that we can possibly compare at the end after removing 3 values
        answer = min(answer, heapq.heappop(four_largest) - heapq.heappop(four_smallest))

    return answer


print(minDifference([1, 5, 0, 10, 14]) == 1)
