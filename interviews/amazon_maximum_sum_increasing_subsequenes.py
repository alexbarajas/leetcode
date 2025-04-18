


def findMaxProducts(products):  # THIS DID NOT WORK, I DIDN'T UNDERSTAND THE QUESTION
    answer = 0
    n = len(products)
    points = [0 for i in range(n)]

    for i in range(n):
        points[i] = products[i]

    for i in range(1, n):
        for j in range(i):
            if products[i] > products[j] and points[i] < points[j] + products[i]:
                points[i] = points[j] + products[i]

    for i in range(n):
        if answer < points[i]:
            answer = points[i]

    return answer


products = [7, 4, 5, 2, 6, 5]
print(findMaxProducts(products))

products = [2, 9, 4, 7, 5, 2]
print(findMaxProducts(products))
