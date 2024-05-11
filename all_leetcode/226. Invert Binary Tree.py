from support.classes import TreeNode
from support.functions import array_to_tree, tree_to_array
from typing import Optional


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    root.left, root.right = invertTree(root.right), invertTree(root.left)

    return root


root = [4, 2, 7, 1, 3, 6, 9]

print(tree_to_array(invertTree(array_to_tree(root))) == [4, 7, 2, 9, 6, 3, 1])
