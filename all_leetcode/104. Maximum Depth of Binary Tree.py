from support.classes import TreeNode
from support.functions import array_to_tree
from typing import Optional


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))


root = [3, 9, 20, None, None, 15, 7]

print(maxDepth(array_to_tree(root)) == 3)
