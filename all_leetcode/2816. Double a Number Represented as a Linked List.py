from support.classes import ListNode
from support.functions import array_to_linkedlist, linkedlist_to_array
from typing import Optional


def doubleIt(head: Optional[ListNode]) -> Optional[ListNode]:
    total = 0
    divider = 1

    while head:
        total *= 10
        total += head.val
        head = head.next
        divider *= 10

    total *= 2

    if divider > total:
        divider //= 10

    dummy = ListNode()
    current = dummy

    while divider:
        current.next = ListNode(total // divider)
        total %= divider
        divider //= 10
        current = current.next

    return dummy.next


print(linkedlist_to_array(doubleIt(array_to_linkedlist([1, 8, 9]))) == [3, 7, 8])
