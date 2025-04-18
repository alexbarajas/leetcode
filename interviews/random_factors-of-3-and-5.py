"""An ideal number is a positive integer that has only 3 and 5 as prime divisors.
An ideal number can be expressed in the form of 3^x * 5^y, where x and y are non-negative integers.
For example, 15, 45 and 75 are ideal numbers but 6, 10, and 21 are not. """

# https://leetcode.com/problems/ugly-number-ii/
# this is similar

def getIdealNums(low, high):  # STILL NEED TO OPTIMIZE THIS SOLUTION
    score = 0  # can be any variable name
    for number in range(low, high + 1):
        for x in range(0, 21):  # I chose 20 as the max value for x since it'll take care of all the values up to 2x10^9
            for _ in range(0, 21):  # should take care of all of the values
                y = x - _  # tries when y > x
                if number == (3 ** x) * (5 ** y):
                    score += 1
                else:
                    y = x + _  # tries the remaining options
                    if number == (3 ** x) * (5 ** y):
                        score += 1
    print(score)  # prints out the answer
    # return score


getIdealNums(1, 100)
