from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_str = ""

        while head:
            bin_str += str(head.val)

            head = head.next

        return int(bin_str, 2)
