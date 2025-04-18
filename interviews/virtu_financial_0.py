"""
Write a function:

def solution(X)

that, given an integer X, returns an integer that corresponds to the
minimum number of steps required to change X to a Fibonacci number.

In each step you can either increment or decrement the current number,
i.e. you can change X to either X+1 or X-1.

X will be between 0 and 1,000,000 inclusive.

the Fibonacci sequence is defined as follows:

F[0] = 0
F[1] = 1

for each i >= 2: F[i] = F[i-1] + F[1-2]

The elements of the Fibonacci sequence are called Fibonacci numbers.

For example, for X = 15 the function should return 2.
For X = 1 and X = 13 the function should return -0.
"""


def solution(X):
    # write your code in Python 3.6
    if X < 2:
        return 0
    n1 = 0
    n2 = 1
    n3 = n1 + n2
    min_steps = float("inf")
    while abs(X - n3) <= min_steps:
        min_steps = abs(X - n3)
        n3 = n1 + n2  # the sum of the rest of the values in the fibonacci function
        n1 = n2
        n2 = n3
    return min_steps


X = 13

print(solution(X))

X = 15

print(solution(X))

X = 21

print(solution(X))
