class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # 0. if there is no head return None
        if not head:
            return None

        # 1. set up a dummy node, and two pointers, left at the dummy before the head, right at the head
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # 2. while n > 0 and right exists, shift right by 1 by decreasing n by 1 until it's 0
        while right and n > 0:
            right = right.next
            n -= 1

        # 3. now that you have the correct distance between the pointers, shift them until right doesn't exist anymore
        while right:
            left = left.next
            right = right.next

        # 4. get rid of left.next by setting it as left.next.next
        left.next = left.next.next

        # 5. return dummy.next
        return dummy.next



# head = [1,2,3,4,5]
# n = 2
# print(Solution().removeNthFromEnd(head, n))

