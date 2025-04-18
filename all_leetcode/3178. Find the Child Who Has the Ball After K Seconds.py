def numberOfChild(n: int, k: int) -> int:
    # # SOLUTION 1: iterative
    # i = 0
    # for _ in range(k):
    #     if i == n - 1:
    #         direction = "left"
    #     elif i == 0:
    #         direction = "right"
    #     i += 1 if direction == "right" else -1

    # return i

    # SOLUTION 2: math
    # each value for n will take (2 * (n - 1)) steps for it to loop the children and return to its original spot
    # so do k %= (2 * (n - 1)) to get the remainder of k after doing the max possible loops
    k %= (2 * (n - 1))
    # a loop has 2 segments, when you move right, and when you move right:
    # moving right: if k < n you won't switch direction so just return k since that's how many times you'll pass the ball
    # moving left: since 2 * (n - 1) is how long a loop takes, return 2 * (n - 1) - k since that's how many times you passed the ball
    return k if k < n else 2 * (n - 1) - k
    # this line below also works and might be easier to understand
    # return k if k < n else (n - 1) - (k - (n - 1))


print(numberOfChild(n=3, k=5) == 1)
print(numberOfChild(n=5, k=6) == 2)
