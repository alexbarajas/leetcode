"""
Dijkstra's algorithm is used to find the shortest paths from a source node to all other nodes in a weighted graph with non-negative weights.

steps for Dijkstra's
1. graph construction
- build the graph representation using adjacency lists or matrices, where nodes and edges are defined
2. initialization of data structures
- set up necessary data structures
3. priority queue (min-heap)
- use this data structure to always process the node with the smallest distance. This helps in efficiently finding and updating the minimum distance node
4. Dijkstra's implementation
- implement the core of the algorithm where you repeatedly extract the node with the smallest distance from the priority queue, update its neighbors, and push these neighbors into the priority queue with updated distances
5. updating values
- for each extracted node, update the distances of its neighboring nodes if a shorter path is found. This involves checking and updating the priority queue
6. final result
- after all nodes have been processed, the distance array will contain the shortest distances from the starting node to each node. Optionally, reconstruct the shortest paths from the starting node to any other node if required
"""

import collections
import heapq


def networkDelayTime(times, n, k):
    # 1. graph construction
    graph = collections.defaultdict(list)
    for u, v, w in times:  # sourceNode, targetNode, time
        graph[u].append((v, w))
        # graph[v].append((u, w))  # include this line only if the graph is undirected

    # 2. initialization of data structures
    visited = set()
    time = 0

    # 3. priority queue (min-heap)
    heap = [(0, k)]  # the heap will contain [pathLength, node], so [0, k] means that the path length is 0, and that makes sense because k is the origin. the pathLength is from the origin, not from the node before it

    # 4. Dijkstra's implementation
    # the heap will go as far from the k node as possible
    while heap:
        # print(heap, visited)
        time1, node1 = heapq.heappop(heap)
        if node1 in visited:
            continue
        visited.add(node1)
        time = max(time, time1)
        # 5. updating values
        for node2, time2 in graph[node1]:
            if node2 not in visited:
                heapq.heappush(heap, (time1 + time2, node2))

    # look at the heap comment above, if len(visited) == n, then that means you can visit every node from the k node, so if it isn't then you can't visit every node, which is why we return -1 in that instance
    return time if len(visited) == n else -1


print(networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2) == 2)
