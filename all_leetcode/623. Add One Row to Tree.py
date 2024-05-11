from support.classes import TreeNode
from support.functions import array_to_tree, tree_to_array
from typing import Optional


def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    # SOLUTION 1: easy to understand
    if depth == 1:
        return TreeNode(val, root, None)

    def dfs(node, level):
        if not node:
            return
        level -= 1
        if level == 1:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)
        else:
            dfs(node.left, level)
            dfs(node.right, level)

    dfs(root, depth)

    return root

    # # SOLUTION 2: also works and uses recursion
    # if depth == 1:
    #     return TreeNode(val, root, None)

    # elif depth == 2:
    #     root.left = TreeNode(val, root.left, None)
    #     root.right = TreeNode(val, None, root.right)
    # else:
    #     if root.left:
    #         self.addOneRow(root.left, val, depth - 1)
    #     if root.right:
    #         self.addOneRow(root.right, val, depth - 1)

    # return root


root = [4, 2, 6, 3, 1, 5]
val = 1
depth = 2

print(tree_to_array(addOneRow(array_to_tree(root), val, depth)) == [4, 1, 1, 2, None, None, 6, 3, 1, 5])
