from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head

        current_node = head
        previous = None

        while current_node.next:
            previous = current_node
            current_node = current_node.next

            if previous and current_node:
                a = previous.val
                b = current_node.val

                while b:
                    a, b = b, a % b

                new_node = ListNode(a)
                new_node.next = current_node
                previous.next = new_node

        return head

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        current_node = head

        while current_node and current_node.next:
            a = current_node.val
            b = current_node.next.val

            while b:
                a, b = b, a % b

            new_node = ListNode(a)
            new_node.next = current_node.next
            current_node.next = new_node

            current_node = new_node.next

        return head
