def valueAfterKSeconds(n: int, k: int) -> int:
    MOD = 10 ** 9 + 7
    array = [1] * n

    for i in range(k):
        for j in range(1, n):
            array[j] += array[j - 1]

    return array[-1] % MOD


print(valueAfterKSeconds(n=4, k=5) == 56)
