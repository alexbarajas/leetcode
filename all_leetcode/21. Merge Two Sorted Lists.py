from support.classes import ListNode
from support.functions import array_to_linkedlist, linkedlist_to_array
from typing import Optional


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # 1. set up a dummy node using dummy = ListNode(), and then set the head as head = dummy, you will set up a new linked list using the empty head node
    dummy = ListNode()
    head = dummy

    # 2. while both lists exist, compare the next values in both lists, add the smallest to the head
    while list1 and list2:
        if list1.val < list2.val:
            head.next = list1
            list1 = list1.next
        else:
            head.next = list2
            list2 = list2.next

        # 2.1. always shift the head pointer after adding a node to it
        head = head.next

    # 3. once one of the lists is done, add the remainder of the list that remains
    head.next = list1 or list2
    # head.next = list1 if list1 else list2 # this also works

    # 4. return dummy.next since it returns the list
    return dummy.next


print(linkedlist_to_array(mergeTwoLists(array_to_linkedlist([1,2,4]), array_to_linkedlist([1,3,4]))) == [1,1,2,3,4,4])
