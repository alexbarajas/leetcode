"""
LeetCode Problem: 2. Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/
Difficulty: Medium
Topics: Linked List, Math
"""

from typing import Optional

from support.classes import ListNode
from support.functions import array_to_linkedlist, linkedlist_to_array


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # 1. set up a dummy node, current node set as the dummy, and a carry variable as 0
    dummy = ListNode(0)
    current = dummy
    carry = 0

    # 2. while l1 or l2 or the carry exist...
    while l1 or l2 or carry:
        # 2.1. get the values from the linked lists, set them to 0 if there are none
        value1 = l1.val if l1 else 0
        value2 = l2.val if l2 else 0

        # 2.2. set the carry, and a remainder variable as the sum of (val1 + val2 + carry), do // for the carry, % for the remainder
        value = value1 + value2 + carry
        carry, remainder = value // 10, value % 10

        # 2.3. set current.next as a node set as the reminder, and then shift the current to that node
        current.next = ListNode(remainder)
        current = current.next

        # 2.4. shift the linked lists that exist, set them as None if they don't
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    # 3. return dummy.next
    return dummy.next


print(linkedlist_to_array(addTwoNumbers(array_to_linkedlist([2, 4, 3]), array_to_linkedlist([5, 6, 4]))) == [7, 0, 8])
