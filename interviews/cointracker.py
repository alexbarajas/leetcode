"""
given an array of dictionaries with photos and when they were upvoted along with a timestamp threshold
the follow-up implemented k instead of not having it
"""

import heapq

photos1 = [
    {"photo_id": "a", "timestamp": 2},
    {"photo_id": "b", "timestamp": 4},
    {"photo_id": "a", "timestamp": 10},
    {"photo_id": "a", "timestamp": 2},
    {"photo_id": "b", "timestamp": 1},
    {"photo_id": "b", "timestamp": 2},
    {"photo_id": "b", "timestamp": 1},
    {"photo_id": "c", "timestamp": 1},
    {"photo_id": "d", "timestamp": 5},
]
timestamp_threshold1 = 2
k1 = 3

photos2 = [
    {"photo_id": "a", "timestamp": 2},
    {"photo_id": "b", "timestamp": 4},
    {"photo_id": "a", "timestamp": 10},
    {"photo_id": "a", "timestamp": 2},
    {"photo_id": "b", "timestamp": 1},
    {"photo_id": "b", "timestamp": 2},
    {"photo_id": "b", "timestamp": 1},
    {"photo_id": "c", "timestamp": 1},
    {"photo_id": "d", "timestamp": 1},
    {"photo_id": "d", "timestamp": 2},
]
timestamp_threshold2 = 2
k2 = 3

photos3 = [
    {"photo_id": "a", "timestamp": 2},
    {"photo_id": "b", "timestamp": 4},
    {"photo_id": "a", "timestamp": 10},
    {"photo_id": "a", "timestamp": 2},
    {"photo_id": "b", "timestamp": 1},
    {"photo_id": "b", "timestamp": 2},
    {"photo_id": "b", "timestamp": 1},
    {"photo_id": "c", "timestamp": 1},
    {"photo_id": "d", "timestamp": 1},
    {"photo_id": "d", "timestamp": 2},
]
timestamp_threshold3 = -1
k3 = 1


def most_upvoted(photos, timestamp_threshold, k):
    photo_upvotes = {}
    for photo in photos:
        if photo["timestamp"] > timestamp_threshold:
            continue
        photo_id = photo["photo_id"]
        photo_upvotes[photo_id] = photo_upvotes.get(photo_id, 0) + 1

    heap = []
    for photo, upvotes in photo_upvotes.items():
        heapq.heappush(heap, (upvotes, photo))
        while len(heap) > k:
            heapq.heappop(heap)

    answer = []
    while heap:
        answer.append(heapq.heappop(heap)[1])

    return answer[::-1]


print(most_upvoted(photos1, timestamp_threshold1, k1) == ["b", "a", "c"])
print(most_upvoted(photos2, timestamp_threshold2, k2) == (["b", "d", "a"] or ["b", "a", "d"]))
print(most_upvoted(photos3, timestamp_threshold3, k3) == [])
