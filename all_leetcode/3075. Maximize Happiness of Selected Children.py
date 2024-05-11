from typing import List


def maximumHappinessSum(happiness: List[int], k: int) -> int:
    answer = 0
    decrements = 0

    happiness.sort(reverse=True)

    for i in range(min(k, len(happiness))):
        answer += max(happiness[i] - decrements, 0)
        decrements += 1

    return answer


print(maximumHappinessSum(happiness=[1, 2, 3], k=2) == 4)
print(maximumHappinessSum(happiness=[1, 1, 1, 1], k=2) == 1)
