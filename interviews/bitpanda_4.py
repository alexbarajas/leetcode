from heapq import heappush, nsmallest
def nth_lowest_selling(sales, n):
    """
    :param elements: (list) List of book sales.
    :param n: (int) The n-th lowest selling element the function should return.
    :returns: (int) The n-th lowest selling book id in the book sales list.
    """
    heap = []
    for number in sales:
        heappush(heap, number)
    choice = nsmallest(n, heap)[-1]
    hashmap = {}
    for number in sales:
        if number not in hashmap:
            hashmap[number] = 1
        else:
            hashmap[number] += 1
    heap2 = []
    for key, value in hashmap.items():
        for i in range(value):
            heappush(heap2, key)

        if value == choice:
            return key

print(nth_lowest_selling([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))
print(nth_lowest_selling([5, 4, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1], 2))


# BRU THIS WAS SO BAD