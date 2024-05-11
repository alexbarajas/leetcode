import heapq


def maxPotholes(road: str, budget: int) -> int:
    end = 0
    n = len(road)
    answer = 0
    heap = []

    while end < n:
        if road[end] != ".":
            start = end
            while end < n and road[end] == "x":
                end += 1
            heapq.heappush(heap, start - end)
        end += 1

    while heap and budget:
        current = min(budget - 1, -heapq.heappop(heap))
        budget -= current + 1
        answer += current

    return answer


print(maxPotholes(road="..", budget=5) == 0)
print(maxPotholes(road="..xxxxx", budget=4) == 3)
print(maxPotholes(road="x.x.xxx...x", budget=14) == 6)
