from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0

        if head:
            current_node = head

            while current_node:
                size += 1
                current_node = current_node.next

            current_node = head
            counter = 0

            while current_node:
                if size % 2 == 0:
                    if counter == size // 2:
                        return current_node

                else:
                    if counter == (size // 2):
                        return current_node

                counter += 1

                current_node = current_node.next

        def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow
