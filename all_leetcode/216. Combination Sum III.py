from typing import List


def combinationSum3(k: int, n: int) -> List[List[int]]:
    # 1. set up an empty answer array
    answer = []

    # 2. set up a backtracking function that takes in the current start value, current combination, and the total for that combination
    def backtracking(start, combination, total):
        # 2.1 if you have k numbers in combination or if total > n, check to see if the total is n so you can append a copy of the current combination to the answer, return at the end regardless
        if len(combination) == k or total > n:
            if total == n:
                answer.append(combination.copy())
            return

        # 2.3 if you can continue, append the next number to combination, and then backtrack using end as the new start, updated combination, and use total + end as the new total
        for end in range(start + 1, min(10, n + 1)):
            combination.append(end)
            backtracking(end, combination, total + end)
            combination.pop()

    # 3. initialize the backtracking function with 0 as start, an empty array as the combination, and 0 as the total
    backtracking(0, [], 0)

    # 4. return the answer
    return answer


print(combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]])
print(combinationSum3(9, 45) == [[1, 2, 3, 4, 5, 6, 7, 8, 9]])
