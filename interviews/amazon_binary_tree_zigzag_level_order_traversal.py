

"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""

from collections import deque
def zigzagLevelOrder(root):
    # if root is None return an empty array, otherwise make an empty answer array
    if root is None:
        return []
    answer = []

    def dfs(node, level):
        # appends to the answer once the level is >= to the length of the answer array
        if level >= len(answer):
            answer.append(deque([node.val]))
        else:
            if level % 2 == 0:  # if even
                answer[level].append(node.val)
            else:  # if odd
                answer[level].appendleft(node.val)

        # continues the function as long as there are next nodes in the next level
        for next_node in [node.left, node.right]:
            if next_node is not None:
                dfs(next_node, level + 1)

    # start the dfs function with the root node and a level of 0
    dfs(root, 0)

    # return the answer array at the end
    return answer

root = [3,9,20,null,null,15,7]
print(zigzagLevelOrder(root))