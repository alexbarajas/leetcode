"""
write a function that, given an integer N, return the max possible value obtained by
deleting one "5" from the decimal representation of N.
"""


def solution(N):
    n = str(N)
    left_answer = None
    right_answer = None
    for num in range(len(n)):
        if n[num] == "5":
            left_answer = n[:num] + n[num + 1:]
            break
    for num in range(len(n)):
        if n[-num] == "5":
            right_answer = n[:-num] + n[-num + 1:]
            break
    if n[0] == "-":
        return int(min(right_answer, left_answer))
    else:
        return int(max(right_answer, left_answer))


    # str_num = str(N)
    # first_num = 0
    # second_num = 0
    #
    # for i in range(len(str_num)):
    #     if str_num[i] == '5':
    #         first_num = int(str_num[0:i] + str_num[i+1:len(str_num)])
    #         break
    #
    # for i in range(len(str_num)-1, -1, -1):
    #     if str_num[i] == '5':
    #         second_num = int(str_num[0:i] + str_num[i+1:len(str_num)])
    #         break
    #
    # return max(first_num, second_num)


N = 15958
print(solution(N))

N = -5859
print(solution(N))













