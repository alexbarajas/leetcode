from support.classes import TreeNode
from support.functions import array_to_tree
from typing import Optional
import heapq


def smallestFromLeaf(root: Optional[TreeNode]) -> str:
    if not root:
        return ""

    real_answer = []

    def dfs(node, current):
        if not node:
            return
        if not node.left and not node.right:
            new = []
            for num in (current.copy() + [node.val])[::-1]:
                new.append(chr(ord("a") + num))
            heapq.heappush(real_answer, "".join(new))
            return
        dfs(node.left, current + [node.val])
        dfs(node.right, current + [node.val])

    dfs(root, [])

    return heapq.heappop(real_answer)


print(smallestFromLeaf(array_to_tree([0, 1, 2, 3, 4, 3, 4])) == "dba")
