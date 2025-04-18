## "Shortest Path" algorithms

we can use the “breadth-first search” algorithm to find the “shortest path” between two vertices. However, the
“breadth-first search” algorithm can only solve the “shortest path” problem in “unweighted graphs”. But in real life, we
often need to find the “shortest path” in a “weighted graph”. This is where Dijkstra's comes in.

“Dijkstra's algorithm” can only be used to solve the “single source shortest path” problem in a graph with non-negative
weights.

“Bellman-Ford algorithm”, on the other hand, can solve the “single-source shortest path” in a weighted directed graph
with any weights, including, of course, negative weights.

## Binary Search Intuition

whenever you see maximise something by minimising, it's binary search problem, an example
is: https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag

