"""
LeetCode Problem: 104. Maximum Depth of Binary Tree
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy
Topics: Binary Tree, DFS
"""

from typing import Optional

from support.classes import TreeNode
from support.functions import array_to_tree


def maxDepth(root: Optional[TreeNode]) -> int:
    # 1. if no root exists then return 0
    if not root:
        return 0

    # 2. in a recursive DFS algorithm, return 1 + the max of the maxDepth of either side, we add 1 to account for the initial node
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


root = [3, 9, 20, None, None, 15, 7]

print(maxDepth(array_to_tree(root)) == 3)
