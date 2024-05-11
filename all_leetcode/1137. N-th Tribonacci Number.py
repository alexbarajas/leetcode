def tribonacci(n: int) -> int:
    x = 0
    y = 1
    z = 1

    for i in range(3, n):
        x, y, z = y, z, x + y + z

    return x + y + z


print(tribonacci(4) == 4)
print(tribonacci(25) == 1389537)
