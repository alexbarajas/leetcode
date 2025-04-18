"""
Given a string of flights to different cities with transfer points in sequence,
chart the shortest paths (i.e. least amount of transfer) to a city given the
origin and destination (there might be multiple shortest paths).
If there is no such path return ‘none’.
"""


def shortestFlight(flights, origin, destination):
    # set up an answer array, and split up the data in the flights string so it's easy to manipulate
    answer = []
    flights = [flight.split(" -> ") for flight in flights.split("\n")]

    # set up a paths hashmap where the start and end of each part of the flight is mapped
    paths = {}
    for flight in flights:
        for i in range(len(flight) - 1):
            if flight[i] not in paths:
                paths[flight[i]] = [flight[i + 1]]
            else:
                paths[flight[i]].append(flight[i + 1])

    # use depth first search to get each possible route for the origin and destination
    def dfs(start, path, stops):
        path.append(start)
        if start in paths:
            if start not in paths:
                return
            if destination in paths[start]:
                path.append(destination)
                answer.append(path)
                return
            for step in paths[start]:
                return dfs(step, path, stops + 1)

    # a base case before the dfs function is initialized. if the origin is not in a possible route, then return None
    if origin not in paths:
        return None

    # start the dfs function if the origin has a possible path in the hashmap
    for stop in paths[origin]:
        dfs(stop, [origin], 1)

    # a base case if there is no complete route for the given origin and destination
    if len(answer) == 0:
        return None

    # get rid of all routes that are not the min steps from the answer array
    min_steps = min(len(route) for route in answer)
    for route in answer[:]:
        if len(route) != min_steps:
            answer.remove(route)

    # finally return the answer array if there is at least one optimal route
    return answer


# flights I used to test the program
flights = "NY -> Iceland -> London -> Berlin\nNY -> Maine -> London\nBerlin -> Paris -> Amsterdam\nParis -> London -> Egypt"  # will give multiple arrays in the answer
# flights = "NY -> Iceland -> London -> NY -> Berlin\nNY -> Maine -> NY -> London\nBerlin -> Paris -> Amsterdam\nParis -> London -> Egypt"  # will remove an array from the answer

origin = "NY"
destination = "Egypt"
print(shortestFlight(flights, origin, destination))  # will return an array of arrays

origin = "NYC"
destination = "Egypt"
print(shortestFlight(flights, origin, destination))  # will return None

origin = "NY"
destination = "New York"
print(shortestFlight(flights, origin, destination))  # will return an array of arrays

flights = ""
origin = "NY"
destination = "New York"
print(shortestFlight(flights, origin, destination))  # will return None