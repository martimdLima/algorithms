from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        values_set = set(nums)

        while head and head.val in values_set:
            head = head.next

        current = head
        prev = None

        while current:
            if current.val in values_set:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return head
