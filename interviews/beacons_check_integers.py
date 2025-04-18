"""
check if A is in B and return the integer where it happens, if not return -1
"""


def solution(A, B):
    A = str(A)
    B = str(B)
    A_length = len(A)
    B_length = len(B)
    if A_length > B_length:
        return -1

    for i in range(B_length - A_length + 1):
        if B[i:i + A_length] == A:
            return i
    return -1

A = 53
B = 1953786
print(solution(A, B))

A = 53
B = 1
print(solution(A, B))

A = 53
B = 483953
print(solution(A, B))