def simplified_garage(n, tickets):
    # n=5, tickets = [1, 4, 1, 0]
    result = [0 for i in range(n)]  # result = [0, 0, 0, 0, 0]

    car_count = {}
    for ticket in tickets:
        car_count[ticket] = car_count.get(ticket, 0) + 1  # updates the car_count hashmap with the counts of each entry time
    # car_count = {0: 1, 1: 2, 4: 1}
    for i in range(n):
        if i == 0:
            result[i] += car_count[i]  # result = [1, 0, 0, 0, 0]
        else:  # 1 -> 4
            car_count[i] = car_count.get(car_count[i], 0) + car_count[
                i - 1]  # car_count = {0: 1, 1: 3, 2: 3, 3: 3, 4: 4}
            result[i] += car_count[i]
    return result