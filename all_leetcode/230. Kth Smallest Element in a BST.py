"""
LeetCode Problem: 230. Kth Smallest Element in a BST
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Difficulty: Medium
Topics: Binary Tree, DFS
"""

import heapq
from typing import Optional

from support.classes import TreeNode
from support.functions import array_to_tree


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    # 0. base case, if a root doesn't exist, return None
    if not root:
        return None

    # 1. set up an answer array as a heap
    answer = []

    # 2. set up a helper function that takes in a node and heappushes the value of that node (if it exists) and then calls the helper function for the left and right brances of the node
    def helper(node):
        if node:
            heapq.heappush(answer, node.val)
            helper(node.left)
            helper(node.right)

    # 3. initialize the helper function
    helper(root)

    # 4. return the last value from the heap using the k smallest values
    return heapq.nsmallest(k, answer)[-1]


print(kthSmallest(array_to_tree([3, 1, 4, None, 2]), k=1) == 1)
print(kthSmallest(array_to_tree([5, 3, 6, 2, 4, None, None, 1]), k=3) == 3)
