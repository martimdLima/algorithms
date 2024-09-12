from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head

        while current:
            stack.append(current.val)
            current = current.next

        tmp = []
        for element in stack:
            while tmp and tmp[-1] < element:
                tmp.pop()
            tmp.append(element)

        new_head = ListNode()
        list_node = new_head

        for value in tmp:
            list_node.next = ListNode(value)
            list_node = list_node.next

        return new_head.next
