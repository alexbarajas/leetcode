from support.classes import TreeNode, ListNode


def array_to_tree(values):
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]

    children = nodes[::-1]
    root = children.pop()

    for node in nodes:
        if node:
            if children:
                node.left = children.pop()
            if children:
                node.right = children.pop()

    return root


def tree_to_array(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Trim any trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


def print_tree(root, level=0, prefix="Root: "):
    if root is None:
        return

    print(" " * (level * 4) + prefix + str(root.val))
    if root.left is not None or root.right is not None:
        print_tree(root.left, level + 1, "L -- ")
        print_tree(root.right, level + 1, "R -- ")


def array_to_linkedlist(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def linkedlist_to_array(head):
    result = []

    current = head
    while current:
        result.append(current.val)
        current = current.next

    return result
