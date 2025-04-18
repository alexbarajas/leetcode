

def triangle(triangles):
    for triangle in triangles:
        triangle = [int(side) for side in triangle]
        a = min(triangle)
        triangle.remove(a)
        b = min(triangle)
        triangle.remove(b)
        c = min(triangle)
        if a ** 2 + b ** 2 == c ** 2:
            return "Right"
        elif a == b or b == c or a == c:
            return "Isosceles"
    return False


triangles = [["36", "30", "36"], ["3", "5", "4"]]
print(triangle(triangles))
