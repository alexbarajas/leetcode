
def merge(intervals):
    # SOLUTION 1:
    if not intervals:
        return []

    intervals.sort(key = lambda i : i[0])
    answer = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] <= answer[-1][1]:
            answer[-1] = [min(answer[-1][0], interval[0]), max(answer[-1][1], interval[1])]
        else:
            answer.append(interval)

    return answer

    # # SOLUTION 2:
    # # 1. sort the intervals from the first value and make an answer array and set it as the first interval
    # intervals.sort(key = lambda i : i[0])  # sort by the first value in the tuple
    # answer = [intervals[0]]
    #
    # # 2. from the 1th interval onwards, set the lastEnd value as the last value in the last interval in answer
    # for start, end in intervals[1:]:
    #     lastEnd = answer[-1][1]  # last value in the last interval in the answer array
    #
    #     # 3. check if the new start is greater, if it is, make a new interval
    #     if start <= lastEnd:
    #         answer[-1][1] = max(lastEnd, end)  # compares the last values of the 2 intervals
    #     # 4. if not, append the new interval
    #     else:
    #         answer.append([start, end])
    #
    # # 5. return the answer array
    # return answer


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))