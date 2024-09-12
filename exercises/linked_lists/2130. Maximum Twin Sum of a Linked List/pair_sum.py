from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return None, None

        max_twin_sum = 0

        slow = head
        fast = head
        prev = None

        # Split linked list in half
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None  # Break the list into two parts

        # reverse one of the halfs
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # iterate over the lists and get the maximum twin sum
        while slow:
            max_twin_sum = max(slow.val + prev.val, max_twin_sum)
            slow = slow.next
            prev = prev.next

        return max_twin_sum
