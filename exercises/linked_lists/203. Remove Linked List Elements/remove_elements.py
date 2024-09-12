from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head or (head.val == val and not head.next):
            return ListNode("")

        previous = ListNode(-1)
        previous.next = head
        current = previous

        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return previous.next
