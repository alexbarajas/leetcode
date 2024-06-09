import datetime


def numSteps(s: str) -> int:
    # SOLUTION 1: naive approach
    n = len(s)
    answer = 0
    value = 0

    for i in range(n):
        current = s[n - i - 1]
        value += 2 ** i if current == "1" else 0

    while value != 1:
        if not value % 2:
            value //= 2
        else:
            value += 1
        answer += 1

    return answer


def numSteps1(s: str) -> int:
    # SOLUTION 2: more efficient approach
    n = len(s)
    answer = 0
    carry = 0

    for i in range(n - 1):
        current = int(s[n - i - 1]) + carry
        # if the current + carry value is even, then you add 1 to answer because if the value is even it only needs 1 action to become odd
        if not current % 2:
            answer += 1
        # if the current + carry value is odd, then you add 2 to answer because you need 2 actions to make it odd again and see if the value == 1, and set the carry to 1
        else:
            answer += 2
            carry = 1

    return answer + carry


# start = datetime.datetime.now()
# print(numSteps("1101") == 6)
# print(numSteps("1101101001") == 15)
# end = datetime.datetime.now()
# print(end - start)
# start1 = datetime.datetime.now()
# print(numSteps1("1101") == 6)
# print(numSteps1("1101101001") == 15)
# end1 = datetime.datetime.now()
# print(end1 - start1)
