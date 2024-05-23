from support.classes import TreeNode
from support.functions import array_to_tree, tree_to_array
from typing import Optional


def removeLeafNodes(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    if root:
        root.left = removeLeafNodes(root.left, target)
        root.right = removeLeafNodes(root.right, target)
        if root.val == target and not root.left and not root.right:
            return None
        return root
    return None


print(tree_to_array(array_to_tree([1, None, 3, None, 4])) == tree_to_array(
    removeLeafNodes(array_to_tree([1, 2, 3, 2, None, 2, 4]), 2)))
print(tree_to_array(array_to_tree([1])) == tree_to_array(removeLeafNodes(array_to_tree([1, 2, None, 2, None, 2]), 2)))
