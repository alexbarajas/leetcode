
def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    def area(a1, a2, b1, b2, c1, c2):
        side1 = ((b1 - a1) ** 2 + (b2 - a2) ** 2) ** 0.5
        side2 = ((c1 - a1) ** 2 + (c2 - a2) ** 2) ** 0.5
        side3 = ((c1 - b1) ** 2 + (c2 - b2) ** 2) ** 0.5
        sides = (side1 + side2 + side3) / 2
        totalArea = (sides * (sides - side1) * (sides - side2) * (sides - side3)) ** 0.5
        return totalArea

    triangle = area(x1, y1, x2, y2, x3, y3)
    triangleP = round(area(x1, y1, x2, y2, xp, yp) + area(x1, y1, x3, y3, xp, yp) + area(x2, y2, x3, y3, xp, yp),
                      4)  # use round to get rid of floating points
    triangleQ = round(area(x1, y1, x2, y2, xq, yq) + area(x1, y1, x3, y3, xq, yq) + area(x2, y2, x3, y3, xq, yq), 9)

    if not triangle:
        return 0
    elif triangle == triangleP and triangle == triangleQ:
        return 3
    elif triangle == triangleP:
        return 1
    elif triangle == triangleQ:
        return 2
    else:
        return 4


x1, y1, x2, y2, x3, y3, xp, yp, xq, yq = 2, 2, 7, 2, 5, 4, 4, 3, 7, 4
print(pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq))
