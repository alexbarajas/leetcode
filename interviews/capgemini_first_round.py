"""
Capgemini interview

given a number Z, state the max area of a rectangle built with Z lines
squares don't count

"""

def test(Z):
    if Z < 6:
        return 0
    result = int(Z)
    if result & 1:
        Z -= 1
    space = Z // 4
    if Z // 2 == Z / 2:
        if 2 * (space + (space + 1)) <= Z:
            return space * (space + 1)
    return (space + 1) * (space - 1)

Z = 9
print(test(Z))

Z = 10
print(test(Z))

Z = 12
print(test(Z))

Z = 14
print(test(Z))

Z = 16
print(test(Z))

Z = 18
print(test(Z))

Z = 20
print(test(Z))

Z = 15
print(test(Z))

"""
9 half of it is 4, so try 1 and 2 and 1 and 3
6: 2
8: 3
10: 6
12: 8
"""

Z = 25
print(test(Z))

