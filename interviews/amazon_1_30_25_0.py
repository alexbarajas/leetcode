def lexicographically_smallest_permutation(data):
    # this works but is not so efficient
    answer = []
    n = len(data)

    def backtrack(current):
        if len(current) == n:
            answer.append(current[:])
            return

        for num in range(1, n + 1):
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()

    backtrack([])

    maximum_gain = 0
    maximum_gain_permutation = None

    for permutation in answer:
        current_gain = 0
        for i in range(n):
            current_gain += (i + 1) * data[permutation[i] - 1]
        if current_gain > maximum_gain:
            maximum_gain = current_gain
            maximum_gain_permutation = permutation
        if current_gain == maximum_gain:
            if not maximum_gain_permutation:
                maximum_gain_permutation = permutation
            else:
                maximum_gain_permutation = min(maximum_gain_permutation, permutation)

    return maximum_gain_permutation


print(lexicographically_smallest_permutation([2, 4, 5, 3]) == [1, 4, 2, 3])
print(lexicographically_smallest_permutation([2, 1, 2]) == [2, 1, 3])
