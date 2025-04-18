# Imagine you are shopping on Amazon.com for some
# good weight lifting equipment. The equipment you
# want has plates of many different weights that you can
# combine to lift.
# The listing on Amazon gives you an array, plates, that
# consists of n different weighted plates, in kilograms.
# There are no two plates with the same weight. The
# element plates['] denotes the weight of the jth plate
# from the top of the stack. You considèr weight lifting
# equipment to be good if the plate at the top is the
# lightest, and the plate at the bottom is the heaviest.
# More formally, the equipment with array plates will be
# called good weight lifting equipment if it satisfies the
# following conditions (assuming the index of the array
# starts from 1):
# plates{1] < plates[i]for all (2 sisn)
# plates[i] < plates[n] for all (1 sis n-1)
# In one move, you can swap the order of adjacent
# plates. Find out the minimum number of moves
# required to form good weight lifting equipment.


def getMinMoves(plates):
    answer = 0
    n = len(plates)
    high = max(plates)
    low = min(plates)
    hashmap = {}

    for i in range(n):
        if plates[i] == high and i != n - 1:
            hashmap[high] = i
            answer += n - 1 - i
        elif plates[i] == low and i != 0:
            hashmap[low] = i
            answer += i

    if len(hashmap) == 2 and hashmap[high] < hashmap[low]:
        answer -= 1

    return answer

plates = [3, 2, 1]
print(getMinMoves(plates))

plates = [2, 4, 3, 1, 6]
print(getMinMoves(plates))

plates = [4, 11, 9, 10, 12]
print(getMinMoves(plates))