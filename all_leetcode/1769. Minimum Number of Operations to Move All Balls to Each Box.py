from typing import List


def minOperations(boxes: str) -> List[int]:
    n = len(boxes)
    answer = [0 for i in range(n)]

    prefixSumLeftBalls = 0  # number of balls on left of current
    prefixSumRightBalls = 0
    prefixSumLeftMoves = 0  # number of moves needed to get balls on left to current
    prefixSumRightMoves = 0

    for i in range(n):
        j = n - i - 1
        answer[i] += prefixSumLeftMoves
        answer[j] += prefixSumRightMoves
        prefixSumLeftBalls += int(boxes[i])
        prefixSumRightBalls += int(boxes[j])
        prefixSumLeftMoves += prefixSumLeftBalls
        prefixSumRightMoves += prefixSumRightBalls

        # print(answer)

    return answer


print(minOperations("110") == [1, 1, 3])
