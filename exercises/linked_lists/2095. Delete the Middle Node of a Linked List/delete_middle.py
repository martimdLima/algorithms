from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use a two-pointer technique, the "slow and fast pointer" method
        slow = head
        fast = head
        previous = None

        while fast is not None and fast.next is not None:
            previous = slow
            slow = slow.next
            fast = fast.next.next

        if previous is None:
            return ListNode("")

        next_ele = slow.next
        previous.next = next_ele

        return head
