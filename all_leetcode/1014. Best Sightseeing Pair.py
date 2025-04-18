from typing import List

def maxScoreSightseeingPair(values: List[int]) -> int:
    current_start = values[0]
    answer = 0

    for i in range(1, len(values)):
        current_end = values[i] - i
        answer = max(answer, current_start + current_end)
        current_start = max(current_start, values[i] + i)

    return answer

print(maxScoreSightseeingPair([8,1,5,2,6]) == 11)