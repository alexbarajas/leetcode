from support.classes import TreeNode
from support.functions import array_to_tree
from typing import Optional, List


def getLonelyNodes(root: Optional[TreeNode]) -> List[int]:
    answer = []

    def dfs(node):
        if not node:
            return
        if node.left and node.right:
            dfs(node.left)
            dfs(node.right)
        elif node.left:
            answer.append(node.left.val)
            dfs(node.left)
        elif node.right:
            answer.append(node.right.val)
            dfs(node.right)

    dfs(root)

    return answer


root1 = [1, 2, 3, None, 4]
root2 = [7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2]
print(getLonelyNodes(array_to_tree(root1)) == [4])
print(getLonelyNodes(array_to_tree(root2)) == [6, 2])
