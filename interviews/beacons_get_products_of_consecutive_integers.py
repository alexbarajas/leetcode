def solution(A, B):
    answer = 0
    top = int(B ** .5) + 1
    bottom = int(A ** .5)

    for i in range(bottom, top):
        if A <= i * (i + 1) <= B:
            answer += 1

    return answer


A = 6
B = 20
print(solution(A, B))

A = 21
B = 29
print(solution(A, B))