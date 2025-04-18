
import heapq
def minMeetingRooms(intervals):
    # 0. base case, if there is no intervals, return 0
    if not intervals:
        return 0

    # 1. sort intervals according to the meeting start time
    intervals.sort(key=lambda x: x[0])

    # 2. create a rooms heap that consists of the end time of the first meeting, and heapify it
    rooms = [intervals[0][1]]
    heapq.heapify(rooms)

    # 3. go thru each interval, and compare the start time for each interval to the first value in the rooms heap
    for interval in intervals[1:]:
        # 3.1 if the interval start time is more or equal to the first value in the heap, aka the times won't interfere, then pop from the heap, getting rid of the old end time
        if rooms[0] <= interval[0]:
            heapq.heappop(rooms)
        # 3.2 regardless, push the end time for the interval into the heap
        heapq.heappush(rooms, interval[1])

    # 4. return the length of the heap
    return len(rooms)

intervals = [[0,30],[5,10],[15,20]]
print(minMeetingRooms(intervals))