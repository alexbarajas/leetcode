def tuple_slice(startIndex, endIndex, tup):
    answer = ""
    for _ in range(startIndex, endIndex):
        answer += str(tup[_])
        if _ != endIndex - 1:
            answer += ","
    return answer

print(tuple_slice(1, 4, (76, 34, 13, 64, 12)))

